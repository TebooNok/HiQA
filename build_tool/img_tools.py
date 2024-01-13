import xml.etree.ElementTree as ET
from whoosh.analysis import Tokenizer, Token
import jieba

def get_adjacent_lines(blocks, block_index):
    """
    Returns two lists: the lines of text before and after the block at block_index.
    Each list contains lines in order from closest to furthest from the block.
    """
    def is_same_line(origin1, origin2):
        # Adjust this threshold if needed
        THRESHOLD = 10
        return abs(origin1[1] - origin2[1]) < THRESHOLD

    def extract_spans_from_blocks(target_blocks):
        spans = []
        for block in target_blocks:
            if 'lines' in block:
                for line in block['lines']:
                    for span in line['spans']:
                        spans.append(span)
        return spans

    def merge_spans_to_lines(spans):
        if not spans:
            return []

        lines = []
        current_line = spans[0]['text']
        current_origin = spans[0]['origin']

        for span in spans[1:]:
            if is_same_line(span['origin'], current_origin):
                current_line += " " + span['text']
            else:
                lines.append(current_line.strip())
                current_line = span['text']
                current_origin = span['origin']

        lines.append(current_line.strip())
        return lines

    spans_before = extract_spans_from_blocks(blocks[:block_index])
    spans_after = extract_spans_from_blocks(blocks[block_index + 1:])

    lines_before = merge_spans_to_lines(spans_before)
    lines_after = merge_spans_to_lines(spans_after)

    return lines_before, lines_after


def get_text_around_image(blocks, image_index,  lang='CN', word_count=50):
    before_lines, after_lines = get_adjacent_lines(blocks, image_index)

    # print(before_lines)
    # print(after_lines)
    text_content = ""
    counter = word_count

    # Process lines before the image
    for line in reversed(before_lines):
        text_content = line + '\n' + text_content
        if lang == 'CN':
            counter -= len(line)
        else:
            counter -= len(line.split(' '))
        if counter <= 0:
            break

    # Reset the word counter for lines after the image
    counter = word_count

    # Process lines after the image
    for line in after_lines:
        text_content += line + '\n'
        if lang == 'CN':
            counter -= len(line)
        else:
            counter -= len(line.split(' '))
        if counter <= 0:
            break

    return text_content.strip()


def get_title_of_image(blocks, image_index, lang='CN'):
    before_lines, after_lines = get_adjacent_lines(blocks, image_index)

    # Search for a title in the lines before the image
    title = None
    for line in reversed(before_lines):
        if lang == 'CN' and '图' in line:
            title = f"title: {line}"
            break
        elif 'figure' in line.lower():
            title = f"title: {line}"
            break

    # Search for a title in the lines after the image
    for line in after_lines:
        if lang == 'CN' and '图 ' in line:
            return f"title: {line}"
        elif 'figure' in line.lower():
            return f"title: {line}"

    if before_lines:
        title = before_lines[-1]
    return title if title else "title: Not Found"


def transform_to_array(trans):
    trans = trans.replace('matrix(', '').replace(')', '').split(',')
    arr = []
    # print(trans)
    for item in trans:
        # print(item, type(item))
        if item[0] == '.':
            arr.append(float('0' + item))
        elif item[0] == '-':
            arr.append(float('-0'+item[1:]))
        else:
            arr.append(float(item))
    return arr


def parse_page_svg(svg, page_id):
    # 解析SVG内容
    root = ET.fromstring(svg)

    # 获取页面大小
    width = int(float(root.get('width').replace('pt', '')))
    height = int(float(root.get('height').replace('pt', '')))

    # 存储clipPaths
    clips = {}
    for clip in root.findall('.//{http://www.w3.org/2000/svg}clipPath'):
        clips[clip.get('id')] = clip

    # 获取SVG下的第一个g标签
    main_g = root.find('{http://www.w3.org/2000/svg}g')

    page_size = f'H{width}V{height}'
    gs = main_g.findall('{http://www.w3.org/2000/svg}g')

    block_id = 0
    img_clips = []
    blocks = []
    cache = ""
    vertical = None
    horizon = None
    # 遍历主g标签下的所有子g标签
    for g in main_g.findall('{http://www.w3.org/2000/svg}g'):

        # 检查第一个子标签是否为"use"标签并且是否有"data-text"属性
        first_child = list(g)[0] if g else None
        if first_child is not None and first_child.tag == "{http://www.w3.org/2000/svg}use" and 'data-text' in first_child.attrib:
            # get all use tags that contains data-text attribute in g tag and print them
            for u in g.findall('{http://www.w3.org/2000/svg}use'):
                if 'data-text' in u.attrib:
                    text_vertical = transform_to_array(u.get('transform'))[5]
                    text_horizon = transform_to_array(u.get('transform'))[4]
                    if vertical is None or abs(text_vertical - vertical) > 10:
                        vertical = text_vertical
                        cache = cache.strip()
                        if cache != "":
                            blocks.append(cache)
                            cache = u.get('data-text')
                            block_id += 1
                    else:
                        # horizon should change
                        if horizon is None or abs(text_horizon - horizon) > 1:
                            horizon = text_horizon
                            cache += u.get('data-text')
            continue

        clip_path = g.get('clip-path')
        if clip_path and '#clip_' in clip_path:
            clip_id = clip_path.split("#")[1].replace(')', '')
            if clip_id in clips:
                path = clips[clip_id].find('.//{http://www.w3.org/2000/svg}path')
                transform = path.get('transform')
                if not transform:
                    continue
                transform = transform.replace('matrix(', '').replace(')', '')
                d = path.get('d')
                trans_height = int(float(transform.split(',')[5]))
                if not (page_size in d or (transform and trans_height == height)):
                    # print(page_size in d)
                    # print(transform and trans_height == height)
                    # print(f"From Transform: {transform}, D: {d}", page_size, trans_height, height)
                    # print(f"From Transform: {transform}, D: {d} in page {page_id}")
                    img_clips.append((transform.split(','), d, page_id, block_id))
                    blocks.append(f'image_{block_id}')
                    block_id += 1
                else:
                    for sub_g in g.findall('.//{http://www.w3.org/2000/svg}g'):
                        sub_clip_path = sub_g.get('clip-path')
                        if sub_clip_path and '#clip_' in sub_clip_path:
                            sub_clip_id = sub_clip_path.split("#")[1].replace(')', '')
                            if sub_clip_id in clips:
                                sub_path = clips[sub_clip_id].find('.//{http://www.w3.org/2000/svg}path')
                                sub_d = sub_path.get('d')
                                sub_transform = sub_path.get('transform')
                                sub_transform = sub_transform.replace('matrix(', '').replace(')', '')
                                subtrans_height = int(float(sub_transform.split(',')[5]))
                                if not (page_size in sub_d or (sub_transform and subtrans_height == height)):
                                    # print(f"From sub Transform: |{sub_transform}|, D: {sub_d} in page {page_id}")
                                    img_clips.append((sub_transform.split(','), sub_d, page_id, block_id))
                                    blocks.append(f'image_{block_id}')
                                    block_id += 1
                                    break
    return img_clips, blocks


def get_svg_text_around_image(blocks, block_id, lang='CN', word_count=50):
    text_content = ""
    counter = word_count

    # Process lines before the image
    for line in reversed(blocks[:block_id]):
        text_content = line + '\n' + text_content
        if lang == 'CN':
            counter -= len(line)
        else:
            counter -= len(line.split(' '))
        if counter <= 0:
            break

    # Reset the word counter for lines after the image
    counter = word_count

    # Process lines after the image
    for line in blocks[block_id+1:]:
        text_content += line + '\n'
        if lang == 'CN':
            counter -= len(line)
        else:
            counter -= len(line.split(' '))
        if counter <= 0:
            break

    return text_content.strip()


def get_svg_title_around_image(blocks, block_id, lang='CN'):
    # Search for a title in the lines before the image
    title = None
    for line in reversed(blocks[:block_id]):
        if lang == 'CN' and '图' in line:
            title = f"title: {line}"
            break
        elif 'figure' in line.lower():
            title = f"title: {line}"
            break

    # Search for a title in the lines after the image
    for line in blocks[block_id+1:]:
        if lang == 'CN' and '图 ' in line:
            return f"title: {line}"
        elif lang == 'CN' and '图' in line:
            return f"title: {line}"
        elif 'figure' in line.lower():
            return f"title: {line}"

    return title if title else "title: Not Found"



class ChineseTokenizer(Tokenizer):
    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):
        t = Token(positions, chars, removestops=removestops, mode=mode,
                  **kwargs)
        seglist = jieba.cut(value, cut_all=True)
        for w in seglist:
            t.original = t.text = w
            t.boost = 1.0
            if positions:
                t.pos = start_pos + value.find(w)
            if chars:
                t.startchar = start_char + value.find(w)
            if chars and positions:
                t.endchar = start_char + value.find(w) + len(w)
            yield t


def ChineseAnalyzer():
    return ChineseTokenizer()


