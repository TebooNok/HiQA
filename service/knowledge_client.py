import os
import random
import tempfile

import chromadb
import tiktoken
import jieba
import pandas as pd
from whoosh.index import open_dir
from whoosh.index import create_in
from PIL import Image
from utils.filter import filter_product_names, filter_knowledge, default_products
import time
from chromadb.config import Settings
from whoosh.qparser import OrGroup
import openai

from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os
from utils.openai_proxy import get_embedding
from utils.tokenizer import ChineseAnalyzer

settings = Settings(allow_reset=True)

ixs = None
collections = None
enemy_collection = None
init_state = False
encoding = None


def get_knowledge(question, max_token, dataset, begin=None, verbose=False):
    if not begin:
        begin = time.time()
    question_embd = get_embedding(question)
    if verbose:
        print('after embedding', time.time() - begin)
    knowledge = retrieve_knowledge(question, question_embd, max_token, dataset, begin, verbose=verbose)
    if verbose:
        print('knowledge length', len(knowledge))
    return knowledge


def reset_by_lucene(question, results, threshold, lucene_weight):
    # ids每一项是个字符串，格式例如：'id0'
    # distances每一项是个浮点数，表示embedding的距离
    # metas每一项是个字典，格式例如：
    # {'filename': 'AN007.csv', 'n_tokens': 304, 'title': '[desc] 如何构建隔离 CAN 方案 __ 集成电源的隔离 CAN 方案 [desc]\r'}
    # documents每一项是个字符串，表示文本内容
    ids = results['ids'][0]
    distances = results['distances'][0]
    metas = results['metadatas'][0]
    documents = results['documents'][0]

    # 归一化 distances 列表
    min_distance = min(distances)
    max_distance = max(distances)
    try:
        normalized_distances = [(distance - min_distance) / (max_distance - min_distance) for distance in distances]
    except ZeroDivisionError:
        result_list = []
        for i in range(len(ids)):
            result_list.append(documents[i])
        return result_list

    result_list = []
    for i in range(len(ids)):
        # 只包括那些 distance 值小于 0.5 的项
        # if normalized_distances[i] <= threshold:
            # 1 - distance = 打分
        result_list.append([ids[i], 1 - normalized_distances[i], metas[i], documents[i]])

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            schema = Schema(id=ID(stored=True), content=TEXT(analyzer=ChineseAnalyzer(), stored=True))
            # schema = Schema(id=ID(stored=True), content=TEXT(stored=True))
            idx = create_in(temp_dir, schema)
            writer = idx.writer()

            for res in result_list:
                writer.add_document(id=res[0], content=res[3])
            writer.commit()

            stopwords = {"的", "了", "和", "是", "就", "都", "而", "及", "与"}

            with idx.searcher() as searcher:
                tokens = jieba.cut(question, cut_all=False)
                filtered_tokens = [token for token in tokens if token not in stopwords]
                or_question = " ".join(filtered_tokens)
                parser = QueryParser("content", idx.schema, group=OrGroup)
                query = parser.parse(or_question)
                query_results = searcher.search(query, limit=None)

                scores = [hit.score for hit in query_results]
                max_score = max(scores) if scores else 1
                normalized_scores = [score / max_score for score in scores]
                id_to_score = {hit["id"]: normalized_scores[i] for i, hit in enumerate(query_results)}
    except Exception as e:
        pass
    for i, res in enumerate(result_list):
        if res[0] in id_to_score:
            result_list[i][1] += id_to_score[res[0]] * lucene_weight

    result_list = sorted(result_list, key=lambda x: x[1], reverse=True)

    string_list = []
    for res in result_list:
        knowledge = "*** New Knowledge Paragraph ***\n" \
                    f"[Source File] {res[2]['filename']} [Source File]\n" \
                    f"[Knowledge Title] {res[2]['title']} [Knowledge Title]\n" \
                    f"[Knowledge Content] {res[3].replace('[desc]', '').replace('---table begin---', '以下为表格:').replace('---table end---', '')} [Knowledge Content]"

        string_list.append(knowledge)

    return string_list


def retrieve_knowledge(question, question_embd, max_token, dataset, begin, verbose=False):
    global init_state
    global collections
    global encoding

    if not init_state:
        init()
        init_state = True

    collection = collections[dataset]
    question = question.upper() # .replace('3741X', '3741').replace('3641X', '3641').replace('3742X', '3741').replace('3642X', '3641')
    if question.__contains__('经销商') or question.__contains__('销售') or question.__contains__('营销'):
        results = collection.query(
            query_embeddings=question_embd,
            n_results=50,
            where_document={"$contains": "经销商"}
        )
    elif dataset == 'Product documents - Chipanalog' and (question.__contains__('竞品') or question.__contains__('替代') or question.__contains__('代替') \
            or question.__contains__('竞对') or question.__contains__('竞争') or question.__contains__('对手') \
            or question.__contains__('功能一样') or question.__contains__('功能相同') or question.__contains__(
        '功能相似') \
            or question.__contains__('替换')):
        results = enemy_collection.query(
            query_embeddings=question_embd,
            n_results=50,
        )
    else:
        results = collection.query(
            query_embeddings=question_embd,
            n_results=50
        )

    if verbose:
        print('after retrieve', time.time() - begin)
    result_list = reset_by_lucene(question, results, threshold=0.5, lucene_weight=0.5)
    if verbose:
        print('after rank by lucene', time.time() - begin)

    returned_values = filter_knowledge(question, result_list)
    # if verbose:
    #     print('after filter knowledge by keywords', time.time() - begin)
    # if len(returned_values) >= 2:
    #     print(len(returned_values))
    #
    #     all_text, sale_list,img_path = returned_values
    #
    #     sales_info = ''
    #     for index, (model, details) in enumerate(sale_list.items()):
    #         price, _, _ = details  # We're ignoring the image paths for now
    #         sales_info = f"{model} 的价格是 {price}\n" + sales_info
    #     if len(sales_info) > 0:
    #         all_text = '\n\n相关产品的价格信息：\n' + sales_info + '\n' + all_text
    # else:
    #     # Handle the case when the number of returned values is not 2
    #
    #     all_text = returned_values[0]
    #     sale_list = {}
    #     img_path=[]
    #     print("oooooooooooooooooooooooo")
    #     print(len(returned_values))

    if verbose:
        print('after filter', time.time() - begin)
    # for text in results['documents'][0]:
    #     all_text += text.replace('[desc]', '') + '\n'
    all_text = returned_values

    # reduce length to max_token
    tokens = encoding.encode(all_text)
    truncated_text = all_text

    max_token = int(max_token)
    while len(tokens) > max_token:
        truncated_text = truncated_text[:-200]
        tokens = encoding.encode(truncated_text)
    if verbose:
        print('after truncate', time.time() - begin)
    return truncated_text


def has_key_words(item, product_in_query):
    name = item[0]
    content = item[1]
    for product in product_in_query:
        if product in name or product in content:
            return True
    return False


def search_images_from_response(user_input, response, dataset, lang='CN', k=1000):
    global ixs
    ix = ixs[dataset]
    if dataset == 'Product documents - Chipanalog':
        directory = 'datasets/1_Chipanalog/'
    else:
        directory = 'datasets/2_Analog_Book/'
    # product_in_query = filter_product_names(user_input, default_products)
    # product_in_response = filter_product_names(response, default_products)
    # # print('product_in_query', product_in_query)
    # # print('product_in_response', product_in_response)
    # if not product_in_query and not product_in_response:
    #     query = user_input + ' ' + response[:min(300, len(response))]
    # if product_in_response:
    #     query = user_input + ' ' + response
    # if product_in_query:
    #     query = user_input

    query = user_input
    # Tokenize the query string and join tokens with OR operator
    if lang == 'CN':
        query_tokens = jieba.cut(query, cut_all=True)
    else:
        query_tokens = query.split()

    or_query = " OR ".join(query_tokens)

    parser = QueryParser("content", ix.schema)
    myquery = parser.parse(or_query)

    with ix.searcher() as searcher:
        results = searcher.search(myquery, limit=k)

        results_list = [(hit['file_name'], hit['content'], hit.score) for hit in results]
        # keywords_result = [item for item in results_list if item[2] > 10 and has_key_words(item, product_in_query)]
        # if len(keywords_result) > 0:
        #     results_list = keywords_result
        images = []
        for result in results_list:
            # print('content:', result[1])
            image_name = result[0]  # name
            base_name = image_name.split('_img')[0]
            image_full_path = directory + 'images/' + base_name + '/' + image_name + '.png'
            img = Image.open(image_full_path)
            try:
                image_title = result[1].split('\n')[0].split(':')[1]
            except IndexError:
                image_title = 'Title not found'

            image_title = remove_repeated_substrings(image_title)
            images.append((img, image_title, result[2], image_name, result[1]))
            # print('--------- image----------')
            # print(result[0], result[1])

        # print('after search:', len(images))
        # do filter image, re-rank all images
        # images_ret = []
        # images_remain = []
        # for image in images:
            # print('title:', image[1])
            # print('name:', image[3])
            # print('content:', image[4])
            # img_desc = image[1] + ' ' + image[3] + ' ' + image[4]
            # add = False
            # for product in product_in_query:
            #     if product in img_desc:
            #         images_ret.append(image)
            #         add = True
            #         break
            # if not add:
            #     images_remain.append(image)

        # print('after input filter:', len(images_ret))
        # print('after input filter remain: ', len(images_remain))

        # images_rrmain = []
        # for image in images_remain:
        #     img_desc = image[1] + ' ' + image[3] + ' ' + image[4]
        #     add = False
        #     for product in product_in_response:
        #         if product in img_desc:
        #             images_ret.append(image)
        #             add = True
        #             break
        #     if not add:
        #         images_rrmain.append(image)
        # print('after output filter:', len(images_ret))
        # print('after input filter remain: ', len(images_rrmain))

        # images_ret.extend(images_rrmain)
        # print('final return: ', len(images_ret))
        # return images_ret

        return images


def remove_repeated_substrings(s):
    def longest_repeated_substring(text):
        n = len(text)
        table = [[0] * n for _ in range(n)]
        longest_substring = ''
        longest_length = 0

        for i in range(n):
            for j in range(i + 1, n):
                if text[i] == text[j]:
                    if i == 0 or j == 0:
                        table[i][j] = 1
                    else:
                        table[i][j] = table[i - 1][j - 1] + 1

                    if table[i][j] > longest_length:
                        longest_substring = text[i - table[i][j] + 1: i + 1]
                        longest_length = table[i][j]
                else:
                    table[i][j] = 0

        return longest_substring

    longest_substring = longest_repeated_substring(s)
    while len(longest_substring) > 2:
        s = s.replace(longest_substring, '', 1)
        longest_substring = longest_repeated_substring(s)

    return s


def init():
    global encoding
    global ixs
    global collections
    global init_state
    global enemy_collection

    if init_state:
        return

    print('init project')
    'or'.join(jieba.cut("pre load"))

    # load whoosh dictionary
    ix_chipanalog = open_dir('datasets/1_Chipanalog/indexes')
    ix_book = open_dir('datasets/2_Analog_Book/indexes')

    ixs = {'Product documents - Chipanalog': ix_chipanalog,
           'Book - Analog integrated circuit design': ix_book}

    embedding_encoding = "cl100k_base"
    encoding = tiktoken.get_encoding(embedding_encoding)

    chroma_client = chromadb.Client(settings=settings)
    chroma_client.reset()
    collection_name_1 = "chipanalog" + str(random.randint(0, 10000))
    collection_name_2 = "analog_book" + str(random.randint(0, 10000))
    collection_name_3 = "financial" + str(random.randint(0, 10000))
    collection_name_4 = "texas" + str(random.randint(0, 10000))

    # try:
    collection_1 = chroma_client.create_collection(name=collection_name_1)
    collection_2 = chroma_client.create_collection(name=collection_name_2)
    collection_3 = chroma_client.create_collection(name=collection_name_3)
    collection_4 = chroma_client.create_collection(name=collection_name_4)
    enemy_collection = chroma_client.create_collection(name=(collection_name_1 + '_enemy'))
    print('collection created')

    # def load_data_to_chromaDB():
    embds = []
    docs = []
    metas = []
    ids = []
    id = 0
    for filename in os.listdir('datasets/1_Chipanalog/embeddings'):
        if filename.endswith('.csv'):
            filepath = os.path.join('datasets/1_Chipanalog/embeddings/', filename)
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
    collection_1.add(embeddings=embds, documents=docs, metadatas=metas, ids=ids)

    # def load_data_to_chromaDB():
    embds = []
    docs = []
    metas = []
    ids = []
    id = 0
    for filename in os.listdir('datasets/2_Analog_Book/embeddings'):
        if filename.endswith('.csv'):
            filepath = os.path.join('datasets/2_Analog_Book/embeddings/', filename)
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
    collection_2.add(embeddings=embds, documents=docs, metadatas=metas, ids=ids)

    # def load_data_to_chromaDB():
    embds = []
    docs = []
    metas = []
    ids = []
    id = 0
    for filename in os.listdir('datasets/3_Annual financial reports/embeddings'):
        if filename.endswith('.csv'):
            filepath = os.path.join('datasets/3_Annual financial reports/embeddings/', filename)
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
    collection_3.add(embeddings=embds, documents=docs, metadatas=metas, ids=ids)

    # def load_data_to_chromaDB():
    embds = []
    docs = []
    metas = []
    ids = []
    id = 0
    for filename in os.listdir('datasets/4_Texas Instruments/embeddings'):
        if filename.endswith('.csv'):
            filepath = os.path.join('datasets/4_Texas Instruments/embeddings/', filename)
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
    collection_4.add(embeddings=embds, documents=docs, metadatas=metas, ids=ids)

    enemy_embds = []
    enemy_docs = []
    enemy_metas = []
    enemy_ids = []
    enemy_id = 0
    filepath = os.path.join('datasets/1_Chipanalog/竞品处理', '竞品.csv')
    df = pd.read_csv(filepath)
    for index, row in df.iterrows():
        section = row['section']
        n_tokens = row['n_tokens']
        embedding = [float(value) for value in row['embedding'][1:-1].split(',')]
        enemy_embds.append(embedding)
        enemy_docs.append(section)
        enemy_ids.append('id' + str(enemy_id))
        enemy_metas.append({'n_tokens': n_tokens, 'filename': filename, 'title': section.split('\n')[0]})
        enemy_id += 1
    print('doc size:', len(docs))
    print('enemy doc size:', len(enemy_docs))


    enemy_collection.add(embeddings=enemy_embds, documents=enemy_docs, metadatas=enemy_metas, ids=enemy_ids)
    collections = {'Product documents - Texas Instruments': collection_4, 'Product documents - Chipanalog': collection_1,
                   'Book - Analog integrated circuit design': collection_2, 'Annual financial reports': collection_3}
    print('load data successful')


if not init_state:
    init()
    init_state = True

