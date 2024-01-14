import fitz
from PIL import Image

# from service.keyword_setting import load_keywords
from utils import *
import jieba
from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
import os
import shutil
from build_tool.img_tools import *
# from app import BASE_DIR
from utils.filter import *


ix = None
writer = None


def load_pdf(kb_name, filename, dpi=300, skip_page_front=0, skip_page_back=1, skip_block=5, lang='CN'):
    """
    Load pdf file, covert to image, description and index it
    :param lang:
    :param skip_block:
    :param skip_page_back:
    :param skip_page_front:
    :param dpi:
    :param file:
    :return:
    """

    directory = os.path.join(r'C:\Users\cxy\PycharmProjects\HiQA\datasets', kb_name)
    file_path = os.path.join(directory, 'pdfs', filename)
    doc = fitz.open(file_path)

    # load pages
    pages = []
    for i in range(doc.page_count):
        page = doc.load_page(i)
        pages.append(page)

    # increase dpi to 300
    dpi = int(dpi)
    scale = dpi / 72  # default dpi of pdf is 72
    matrix = fitz.Matrix(scale, scale)
    skip_block = int(skip_block)

    base_name = filename.split('.pdf')[0]
    path_name = os.path.join(directory, 'images', base_name)
    if os.path.exists(path_name):
        shutil.rmtree(path_name)
    os.mkdir(path_name)

    for page in pages[int(skip_page_front):-int(skip_page_back)]:  # skip final page

        # part1: get image with description in png-pdf
        p1dict = page.get_text('dict')
        blocks = p1dict['blocks']
        page_pix = page.get_pixmap(matrix=matrix, dpi=dpi)
        page_im = Image.frombytes("RGB", (page_pix.width, page_pix.height), page_pix.samples)

        saved = []  # need to remove if inner a svg image
        for i, block in enumerate(blocks[int(skip_block):]):  # head and tail of pages should be ignore
            if 'image' in block:
                # try:
                    bbox = block['bbox']
                    # skip image that width=398 and hight=137 -> Typically LOGO
                    # TODO skip some special case
                    # if (bbox[2] - bbox[0])*scale - LOGO_WIDTH <= 10 and (bbox[3] - bbox[1])*scale - LOGO_HEIGHT <= 10:
                    #     continue
                    # Scale the bbox coordinates
                    cropped = page_im.crop([int(i * scale) for i in bbox])
                    number = block['number']

                    file_name = path_name + f'/{base_name}_imgbmp_{page.number}_{number}'
                    image_name = file_name + '.png'
                    # print(image_name)
                    try:
                        cropped.save(image_name)
                    except:
                        continue
                    # # Handle text extraction around the image
                    text_content = get_text_around_image(blocks[skip_block:], i, lang)
                    title = get_title_of_image(blocks[skip_block:], i, lang)
                    # print(text_content[:30])
                    # print(title)
                    with open(f'{file_name}.txt', 'w', encoding='utf-8') as text_file:
                        text_file.write(title + '\n' + text_content.replace('\n', ' ')+ f'\nbase name:{base_name}')

                    saved.append((file_name, [int(i * scale) for i in bbox]))
                # except:
                #     pass

        # part2: get image with description in svg-pdf
        try:
            svg = page.get_svg_image(matrix=fitz.Identity)
            image_clips, svg_blocks = parse_page_svg(svg, page.number)
            for clip in image_clips:

                transform = []
                for item in clip[0]:
                    # print(item, type(item))
                    if item[0] == '.':
                        transform.append(float('0' + item))
                    elif item[0] == '-':
                        transform.append(float('-0' + item[1:]))
                    else:
                        transform.append(float(item))
                d = clip[1]
                page_id = clip[2]
                block_id = clip[3]
                matches = re.findall(r'H(\d+\.?\d*)V(\d+\.?\d*)', d)
                float_values = [float(value) for value in matches[0]]
                box_width = float_values[0]
                box_height = float_values[1]
                width_scale = transform[0]
                height_scale = transform[3]
                width_move = transform[4]
                height_move = transform[5]
                x1 = width_move * scale
                y1 = height_move * scale
                # x1=347*scale
                # y1=587*scale
                x2 = x1 + box_width * width_scale * scale
                y2 = y1 + box_height * height_scale * scale

                if y1 > y2:
                    y1, y2 = y2, y1

                # print(x1, y1, x2, y2)
                # 3. 截取并保存图像

                # check images in saved, if in or similar, delete it from file system
                for i, (file_name, bbox) in enumerate(saved):
                    if (abs(bbox[0] - x1) < 10\
                            and abs(bbox[1] - y1) < 10\
                            and abs(bbox[2] - x2) < 10\
                            and abs(bbox[3] - y2) < 10) or \
                            (bbox[0]>x1-10 and bbox[1]>y1-10 and bbox[2]<x2+10 and bbox[3]<y2+10):
                        os.remove(file_name + '.png')
                        os.remove(file_name + '.txt')
                        saved.pop(i)
                        break

                cropped_img = page_im.crop((int(x1), int(y1), int(x2), int(y2)))
                file_name = path_name + f'/{base_name}_imgsvg_{page.number}_{block_id}'
                image_name = file_name + '.png'
                cropped_img.save(image_name)

                # search title and text
                text_content = get_svg_text_around_image(svg_blocks, block_id, lang)
                title = get_svg_title_around_image(svg_blocks, block_id, lang)
                with open(f'{file_name}.txt', 'w', encoding='utf-8') as text_file:
                    text_file.write(title + '\n' + text_content.replace('\n', ' ') + f'\nbase name:{base_name}')
        except Exception as e:
            # some page dont have svg image
            pass
    return path_name


def build_index(kb_name, lang='CN'):
    # Define the schema for the index
    if lang == 'CN':
        schema = Schema(file_name=ID(stored=True), content=TEXT(analyzer=ChineseAnalyzer(), stored=True))
    else:
        schema = Schema(file_name=ID(stored=True), content=TEXT(stored=True))

    # directory = os.path.join('datasets', kb_name)
    directory = os.path.join(r'C:\Users\cxy\PycharmProjects\HiQA\datasets', kb_name)
    index_path = os.path.join(directory, 'indexes')

    # Create an index in a directory
    if os.path.exists(index_path):
        shutil.rmtree(index_path)
    os.mkdir(index_path)
    # temp_index_dir = index_path
    # temp_index_dir = tempfile.mkdtemp(prefix='index_')

    global ix
    if ix is None:
        ix = create_in(index_path, schema)
    global writer
    if writer is None:
        writer = ix.writer()

    # Add documents to the index
    # base_name = os.path.basename(file).split('.')[0]
    # image_path = f'images{base_name}'
    # writer = ix.writer()
    img_path = os.path.join(directory, 'images')
    for filename in os.listdir(img_path):
        file_path = os.path.join(img_path, filename)
        for file in os.listdir(file_path):
            if file.endswith('.txt'):
                doc_path = os.path.join(file_path, file)
                try:
                    with open(doc_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    writer.add_document(file_name=file[:-4], content=content)
                except Exception as e:
                    print(doc_path)
                    pass
            # print('==========')
            # print(content)
            # print("==========")

    # writer.commit()
    # return ix


def search_images_from_response(kb_name, user_input, response, lang='CN', k=20):

    global ix
    if ix is None:
        ix = open_dir(os.path.join(BASE_DIR, 'file_system', kb_name, 'indexes'))
    directory = os.path.join(BASE_DIR, 'file_system', kb_name)
    images_path = os.path.join(directory, 'images')

    keywords = load_keywords(kb_name)
    product_in_query = filter_product_names(user_input, keywords)
    if response:
        product_in_response = filter_product_names(response, keywords)
    else:
        product_in_response = None
    # print('product_in_query', product_in_query)
    # print('product_in_response', product_in_response)
    if not product_in_query and not product_in_response:
        query = user_input + ' ' + response
    if product_in_response:
        query = response
    if product_in_query:
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
        images = []
        for result in results_list:
            # print('content:', result[1])
            image_name = result[0] # name
            base_name = image_name.split('_img')[0]
            image_full_path = os.path.join(images_path, base_name, image_name + '.png')
            img = Image.open(image_full_path)
            try:
                image_title = result[1].split('\n')[0].split(':')[1]
            except IndexError:
                image_title = 'Title not found'
            images.append((img, image_title, result[2], image_name, result[1], image_full_path))
            # print('--------- image----------')
            # print(result[0], result[1])

        # print('after search:', len(images))
        # do filter image, re-rank all images
        images_ret = []
        images_remain = []
        for image in images:
            # print('title:', image[1])
            # print('name:', image[3])
            # print('content:', image[4])
            img_desc = image[1]+' '+image[3] + ' '+image[4]
            add = False
            for product in product_in_query:
                if product in img_desc:
                    images_ret.append(image)
                    add = True
                    break
            if not add:
                images_remain.append(image)

        # print('after input filter:', len(images_ret))
        # print('after input filter remain: ', len(images_remain))

        images_rrmain = []
        for image in images_remain:
            img_desc = image[1]+' '+image[3] + ' '+image[4]
            add = False
            for product in product_in_response:
                if product in img_desc:
                    images_ret.append(image)
                    add = True
                    break
            if not add:
                images_rrmain.append(image)
        # print('after output filter:', len(images_ret))
        # print('after input filter remain: ', len(images_rrmain))

        images_ret.extend(images_rrmain)
        # print('final return: ', len(images_ret))
        return images_ret

# file = 'CA-IS372x-datasheet_cn.pdf'
# # file = 'CA-IS3086 datasheet_cn.pdf'
# temp_image_dir = load_pdf(file, lang='CN')
# print(temp_image_dir)
# ix, temp_index_dir = build_index(file, temp_image_dir)
# results_list = search(ix, "波形", lang='CN', k=10)
# ret_img = return_image(file, results_list, temp_image_dir)
# print('title: ' + ret_img[0])
# ret_img[1].show()

# print(os.listdir('using_pdfs'))

# import tqdm
# for file in tqdm.tqdm(os.listdir('../datasets/4_Texas Instruments/pdfs')):
#     load_pdf('4_Texas Instruments', file)
# build_index('4_Texas Instruments')
#
# writer.commit()
# from whoosh.index import open_dir
# search_ix = open_dir('indexes')
# query = "IF-428x接收端阈值"
# results = search(search_ix, query, lang='CN', k=10)
# for result in results:
#     print(result)
#
# from PIL import Image
#
# for result in results:
#     image_name = result[0]
#     base_name = image_name.split('_img')[0]
#     img = Image.open('images/' + base_name + '/' + image_name + '.png')
#     image_title = result[1].split('\n')[0].split(':')[1]
#     img.show(title=image_title)

# query = "CA-IF428x是什么"
# response = "川土微为您提供的答案是：CA-IF428x 是一款符合家庭总线标准的全集成收发机，其电源和数据共用一对双绞线。CA-IF428x 支持超过 200kbps的数据传输，包含动态电缆匹配电阻，可调的接收端阈值及滞回，可调的发射端摆率等特性以改善复杂应用时的信号完整性等。"
# print(search_images_from_response('test_kb', query, response))
