import base64
import io
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from flask import Flask, stream_template, request, Response, jsonify, send_file

import requests
from service.knowledge_service import *
from werkzeug.utils import secure_filename
from utils.md2csv import md2sections

from utils.openai_proxy import send_messages
from flask_cors import CORS

from utils.section2embedding import section_to_embed
from service.image_service import *
from service.keyword_setting import *

from utils.pdf2md import pdf2md
import log_config
import logging
from datetime import datetime

# 使用日志
logger = logging.getLogger(__name__)
logger.info("This is an info message.")
app = Flask(__name__)
CORS(app, origins='*')

knowledge_retrieval_instances = {}

# 添加 file_system和static 文件夹为静态资源目录，可以直接访问
app.static_folder = 'file_system'


@app.route('/user_query', methods=['POST'])
def chat():
    kb_name = request.json['kb_name']
    if kb_name not in knowledge_retrieval_instances:
        knowledge_retrieval_instances[kb_name] = KnowledgeRetrieval(kb_name=kb_name)
    knowledge_retrieval_instance = knowledge_retrieval_instances[kb_name]

    if request.method == 'POST':
        user_input = request.json['user_input']
        knowledge = knowledge_retrieval_instance.retrieve_knowledge(user_input, time.time())

        def event_stream():
            for line in send_messages(user_input, knowledge):
                print(line)
                text = line.choices[0].delta.get('content', '')
                if len(text):
                    yield text

        return Response(event_stream(), mimetype='text/event-stream')
    else:
        return stream_template('chat.html')


@app.route('/get_knowledge', methods=['POST'])
def knowledge():
    kb_name = request.json['kb_name']
    if kb_name not in knowledge_retrieval_instances:
        knowledge_retrieval_instances[kb_name] = KnowledgeRetrieval(kb_name=kb_name)
    knowledge_retrieval_instance = knowledge_retrieval_instances[kb_name]

    top_k = request.args.get('top_k', 1)

    if request.method == 'POST':
        user_input = request.json['user_input']
        knowledge = knowledge_retrieval_instance.retrieve_knowledge(user_input, time.time())

        return jsonify({"prompt": knowledge})
    else:
        return stream_template('chat.html')


ALLOWED_EXTENSIONS = {'pdf', 'md', 'csv'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/create_knowledge_base', methods=['POST'])
def create_knowledge_base():
    name = request.form.get('name')
    return jsonify(create_knowledge_base_service(name))


@app.route('/list_knowledge_base', methods=['POST'])
def list_knowledge_base():
    return jsonify(list_knowledge_base_service())


@app.route('/remove_knowledge_base', methods=['POST'])
def remove_knowledge_base():
    name = request.json['name']
    return jsonify(remove_knowledge_base_service(name))


@app.route('/update_kb/<kb_name>', methods=['POST'])
def update_knowledge_base(kb_name):
    name = request.json['name']
    return jsonify(remove_knowledge_base_service(name))


@app.route('/upload_pdf/<kb_name>', methods=['POST'])
def upload_pdf(kb_name):
    global knowledge_retrieval_instances
    knowledge_retrieval_instances.pop(kb_name, None)
    # 检查是否有文件部分
    if 'file' not in request.files:
        return jsonify({"error": "No file part."})
    file = request.files['file']
    # 如果用户没有选择文件，则浏览器也会提交一个空部分，所以需要检查文件名
    if file.filename == '':
        return jsonify({"error": "No selected file."})
    if file and allowed_file(file.filename):
        # 将文件内容读取到内存中
        file_data = file.read()
        return jsonify(upload_file_service(file_data, file.filename, kb_name))
    else:
        return jsonify({"error": "Invalid file type."})


@app.route('/task_status/<task_id>', methods=['GET'])
def task_status(task_id):
    status = get_task_status(task_id)
    return jsonify(status)



@app.route('/set_keywords/<kb_name>', methods=['POST'])
def set_keywords(kb_name):
    try:
        keywords = request.json['keywords']
        unkeywords = request.json['unkeywords']
        save_keywords(kb_name, keywords)
        save_unkeywords(kb_name, unkeywords)
        return jsonify({"message": "Keywords saved successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/get_keywords/<kb_name>', methods=['GET'])
def get_keywords(kb_name):
    try:
        keywords = load_keywords(kb_name)
        unkeywords = load_unkeywords(kb_name)
        return jsonify({"keywords": keywords, "unkeywords": unkeywords})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/pdf2img/<kb_name>', methods=['POST'])
def pdf_to_img(kb_name, file_name):
    # Load the PDF and convert to images
    # TODO complete it when upload pdf
    load_pdf(kb_name, file_name, lang='CN')

    return jsonify({"message": "Index built successfully"}), 200


@app.route('/build_index/<kb_name>', methods=['POST'])
def build_search_index(kb_name):
    # Build the index for the images
    build_index(kb_name, lang='CN')

    return jsonify({"message": "Index built successfully"}), 200


@app.route('/search_image/<kb_name>', methods=['GET'])
def search_img(kb_name):
    query = request.form.get('query')
    response = request.form.get('response', None)
    top_k = request.args.get('top_k', 1)

    # Search for the images matching the query
    images = search_images_from_response(kb_name, query, response, lang='CN', k=10)

    ret_title = None
    ret_img = None
    for img, title, score, file_name, content in images[:top_k]:
        file_name = '_'.join(file_name.split('_')[:-3])
        ret_img = img
        if title != 'Title not found':
            ret_title = "Source - " + file_name + ",\t" + title
        else:
            ret_title = "Source - " + file_name

    buffered = io.BytesIO()
    ret_img.save(buffered, format="JPEG")

    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Return the image and title
    return jsonify({"title": ret_title, "image": img_str}), 200


@app.route('/search_image_source/<kb_name>', methods=['POST'])
def search_img_source(kb_name):
    query = request.json['query']
    response = request.json['response']
    top_k = request.args.get('top_k', 1)
    # Search for the images matching the query
    images = search_images_from_response(kb_name, query, response, lang='CN', k=10)
    print(images)
    ret_title = None
    ret_img = None
    for img, title, score, file_name, content, image_full_path in images[:top_k]:
        file_name = '_'.join(file_name.split('_')[:-3])
        ret_img = img
        if title != 'Title not found':
            ret_title = "Source - " + file_name + ",\t" + title
        else:
            ret_title = "Source - " + file_name

    # /Users/apex/MonoProject/fastqa_cloud/file_system/test_kb/images/CA-IF428x_datasheet_Version1/CA-IF428x_datasheet_Version1_imgbmp_6.png",
    # http://127.0.0.1:5000/static/test_kb/images/CA-IF4420S_datasheet_cn_version%201/CA-IF4420S_datasheet_cn_version%201_imgbmp1.png
    image_full_path = image_full_path.split('file_system')[-1]
    image_full_path = 'http://180.184.215.48:8507/static' + image_full_path

    # Return the image and title
    return jsonify({"prompt": "image_title：'" + ret_title + "'，image_path： '" + image_full_path + "'"}), 200


@app.route('/get_md/<kb_name>', methods=['POST'])
def get_markdown(kb_name):
    file_name = request.json['file_name']
    # return the markdown file
    file_path = os.path.join(BASE_DIR, 'file_system', kb_name, 'mds', file_name)

    return send_file(file_path, as_attachment=True)

@app.route('/list_md/<kb_name>', methods=['POST'])
def list_markdown(kb_name):
    file_path = os.path.join(BASE_DIR, 'file_system', kb_name, 'mds')

    file_details = []
    for file in os.listdir(file_path):
        full_path = os.path.join(file_path, file)

        # 获取文件的最后修改时间
        modified_time = os.path.getmtime(full_path)
        modified_time_str = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')

        # 获取文件的大小（以字节为单位）
        size = os.path.getsize(full_path)

        file_details.append({"name": file, "last_modified": modified_time_str, "size": size})

    return jsonify({"file_list": file_details})

@app.route('/list_pdf/<kb_name>', methods=['POST'])
def list_pdf(kb_name):
    file_path = os.path.join(BASE_DIR, 'file_system', kb_name, 'pdfs')

    file_details = []
    for file in os.listdir(file_path):
        full_path = os.path.join(file_path, file)

        # 获取文件的最后修改时间
        modified_time = os.path.getmtime(full_path)
        modified_time_str = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')

        # 获取文件的大小（以字节为单位）
        size = os.path.getsize(full_path)

        file_details.append({"name": file, "last_modified": modified_time_str, "size": size})

    return jsonify({"file_list": file_details})

@app.route('/save_md/<kb_name>', methods=['POST'])
def save_markdown(kb_name):
    global knowledge_retrieval_instances
    knowledge_retrieval_instances.pop(kb_name, None)

    if 'file' not in request.files:
        return jsonify({"error": "No file part."})
    file = request.files['file']
    # 如果用户没有选择文件，则浏览器也会提交一个空部分，所以需要检查文件名
    if file.filename == '':
        return jsonify({"error": "No selected file."})
    if file and allowed_file(file.filename):

        file_data = file.read()
        return jsonify(upload_file_service(file_data, file.filename, kb_name))

    else:
        return jsonify({"error": "Invalid file type."})


if __name__ == '__main__':
    app.run(debug=True, port=8507, host='0.0.0.0')
