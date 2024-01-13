from app import BASE_DIR
import os
import shutil
import os
import chromadb
import tiktoken
import jieba
import pandas as pd
from whoosh.index import open_dir
from utils.filter import *
import time
from openai.embeddings_utils import get_embedding
from service.keyword_setting import *
import logging
from utils.pdf2md import *
from utils.md2csv import *
from utils.section2embedding import section_to_embed
import logging
from concurrent.futures import ThreadPoolExecutor
import uuid

logger = logging.getLogger(__name__)
logger.info("Logging from knowledge_service.")


def list_knowledge_base_service():
    knowledge_base_dir = os.path.join(BASE_DIR, 'file_system')
    knowledge_base_list = os.listdir(knowledge_base_dir)
    return knowledge_base_list


def create_knowledge_base_service(name):
    full_path = os.path.join(BASE_DIR, 'file_system', name)
    # 子目录列表
    subdirs = ['embedded', 'images', 'index', 'mds', 'pdfs', 'sections']
    try:
        # 如果路径不存在，则创建目录
        if not os.path.exists(full_path):
            os.makedirs(full_path)

            # 创建每个子目录
            for subdir in subdirs:
                os.makedirs(os.path.join(full_path, subdir))
        return {"message": f"Knowledge base {name} created successfully.", "path": full_path}
    except Exception as e:
        return {"error": str(e)}


def remove_knowledge_base_service(name):
    full_path = os.path.join(BASE_DIR, 'file_system', name)

    try:
        # 如果路径存在，则删除目录
        if os.path.exists(full_path):
            shutil.rmtree(full_path)
            return {"message": f"Knowledge base {name} removed successfully."}
        else:
            return {"error": f"Knowledge base {name} does not exist."}
    except Exception as e:
        logger.error(f"remove_knowledge_base_service{e}")
        return {"error": str(e)}



# 存储所有的 Future 对象
futures_dict = {}


def save_file_logic(extension,file_data,full_path,filename, kb_name):
    name = os.path.splitext(filename)[0]

    try:
        if not os.path.exists(full_path):
            os.makedirs(full_path)

        with open(os.path.join(full_path, filename), 'wb') as f:
            f.write(file_data)
        if extension=='.pdf':
            pdf2md(kb_name, name)
        md2sections(kb_name, name + '.md')
        section_to_embed(kb_name, name + '.csv', 800)
        return "completed"
    except Exception as e:
        logger.error(f"保存文件时出错: {e}")
        raise RuntimeError("保存文件时出错 error") from e  # 重新抛出异常


def upload_file_service(file_data, filename, kb_name):

    executor = ThreadPoolExecutor(max_workers=8)

    try:
        extension = os.path.splitext(filename)[1]
        if extension==".pdf":
            full_path = os.path.join(BASE_DIR, 'file_system', kb_name, 'pdfs')
        elif extension == ".md":
            full_path = os.path.join(BASE_DIR, 'file_system', kb_name, 'mds')

        file_path = os.path.join(full_path, filename)
        # 在主线程中保存文件

        future = executor.submit(save_file_logic, extension, file_data, full_path, filename, kb_name)
        # 为每个任务生成一个唯一的ID
        task_id = str(uuid.uuid4())
        futures_dict[task_id] = future

        return {
            "message": f"文件的上传过程已开始，路径为 {kb_name}",
            "path": file_path,
            "task_id": task_id  # 返回任务的唯一ID
        }
    except Exception as e:
        logger.error(f"upload_file_service中出错: {e}")
        return {"error": "处理文件时发生内部服务器错误。"}
    finally:
        # 添加对于线程池的清理
        executor.shutdown(wait=False)


def get_task_status(task_id):
    """查询给定任务的状态"""
    future = futures_dict.get(task_id)
    if not future:
        return {"error": "任务ID不存在"}
    elif not future.done():
        return {"status": "任务还在进行中"}
    elif future.exception() is not None:
        # 如果 Future 对象中有异常信息，则返回异常信息
        return {"status": "任务完成", "error": str(future.exception())}
    else:
        # 如果任务成功完成，返回结果
        return {"task_completed": future.done(), "result": future.result()}


class KnowledgeRetrieval:

    def __init__(self, kb_name):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        api_base = os.getenv("OPENAI_API_BASE")
        self.encoding = None
        self.ix = None
        self.collection = None
        self.init_state = False
        self.embedding_model = "text-embedding-ada-002"
        self.openai_api_key = api_key
        self.openai_api_base = api_base
        self.kb_name = kb_name

    def init(self):
        'or'.join(jieba.cut("pre load"))
        # load whoosh dictionary
        # self.ix = open_dir('indexes')
        embedding_encoding = "cl100k_base"
        self.encoding = tiktoken.get_encoding(embedding_encoding)

        chroma_client = chromadb.Client()
        collection_name = self.kb_name
        try:
            chroma_client.delete_collection(name=collection_name)
        except:
            pass

        try:
            self.collection = chroma_client.create_collection(name=collection_name)
        except:
            try:
                self.collection = chroma_client.get_collection(name=collection_name)
            except:
                pass
        # load data
        self.load_data_to_chromaDB()
        self.init_state = True

    def load_data_to_chromaDB(self):
        embds = []
        docs = []
        metas = []
        ids = []
        id = 0
        for filename in os.listdir("file_system/" + self.kb_name + '/embedded/'):
            if filename.endswith('.csv'):
                filepath = os.path.join("file_system/" + self.kb_name + '/embedded/', filename)
                df = pd.read_csv(filepath)
                for index, row in df.iterrows():
                    section = row['section']
                    n_tokens = row['n_tokens']
                    embedding = [float(value) for value in row['embedding'][1:-1].split(',')]
                    embds.append(embedding)
                    docs.append(section)
                    ids.append('id' + str(id))
                    metas.append({'n_tokens': n_tokens, 'filename': filename, 'title': section.split('\n')[0]})
                    id += 1
        try:
            self.collection.add(embeddings=embds, documents=docs, metadatas=metas, ids=ids)
            print('load data successful')

        except:
            pass

    def retrieve_knowledge(self, question, begin):
        question_embd = get_embedding(question, engine=self.embedding_model)
        if not self.init_state:
            self.init()

        results = self.collection.query(
            query_embeddings=question_embd,
            n_results=50
        )

        print('after retrieve', time.time() - begin)
        default_keyword = load_keywords(kb_name=self.kb_name)
        default_unkeyword = load_unkeywords(kb_name=self.kb_name)
        returned_values = filter_knowledge(question, results, default_keyword, default_unkeyword)
        all_text = returned_values[0]

        print('after filter', time.time() - begin)

        tokens = self.encoding.encode(all_text)
        max_tokens = 20000
        truncated_text = all_text

        while len(tokens) > max_tokens:
            truncated_text = truncated_text[:-200]
            tokens = self.encoding.encode(truncated_text)
        return truncated_text
