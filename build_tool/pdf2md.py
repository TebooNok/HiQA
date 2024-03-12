import fitz  # PyMuPDF
import os

import tqdm

import os
import openai
import time
from dotenv import load_dotenv

embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
# set openai
load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')
openai.api_base = os.environ.get('OPENAI_API_BASE')


def extract_text_from_pdf(file_name):
    doc = fitz.open(file_name)
    text = ""
    for page in doc:
        # if page.number < section2begin:
        #     continue
        # if section2end < page.number < finance_begin:
        #     continue
        page_text = page.get_text()
        # page_text = page_text.replace(header, '')
        text += page_text
    return text


def get_message(query):
    prompt = f"""请帮我修改内容格式，我会给你一个PDF文档，文档中的文本可能是文字段落也可能来自表格。请将这些内容转换为markdown格式源码，且输出只有markdown源码，其他要求如下：
1. 无需考虑图片，只提取文字和表格
2. 要求格式为，PDF文本中的每一章节都作为markdown中的一个一级标题(只用一个 # 号)章节，无论章节还是子章节的标题，都要用markdown的一级标题表示，我们将用章节的编号来标记章节的级别。该章节的内容从这一章节的标题的后一行开始写。
3. 重点是准确识别文本中的章节编号和表格，表格格式请仔细处理。
4. 关于章节和编号，对于PDF中的一切章节，子章节，都要在markdown中对应一个一级标题章节（一个# 章节）并且用章节的编号来表示级别，而非多个#，章节编号均为"x.x.x. XXXX"的格式
5. 关于表格，一旦遇你认为是表格，请处理成如下格式，表格内容用markdown的格式源码，但前后不要换行：
---table begin---
Table tile: Name of Table
| column0 | column1 | column2 |
|---|---|---|
| row1 | value | value |
| row2 | value | value |
---table end---
说明：表格的前后由"---table begin---"和"---table end---"包裹，"---table begin---"的下一行是表名。
在提供的文本中，表格会被处理成每个cell一行，当你发现内容是表格时，请重新将其排列为markdown的表格格式。
此外，表格所在的段落也应有独立的标题。
6. 转换后的每个章节中只能有一个表格，如果有多段表格，请为每一个表格设置一个新章节，放置这个表格，并且设置合适的标题。
7. 输出内容只包含markdown源码，不要输出任何其他内容。markdown源码前后不要有说明和补充。
8. 你是一个支持超长文本的模型，你的任务是格式处理，因此不要省略、总结、丢弃任何内容，只要是输入的内容，也包括表格内容，都要在输出中体现出来。
9. 不要带 '```', 'markdown' 这种多余内容
10. 请谨慎使用 '#' 符号，这代表后面是一个独立章节的编号和标题。请正确，准确的使用'#'号设置章节。这一章节的内容从标题的后一行开始写。
11. 请为每个章节设置一个准确、简要的标题。如果原文中有合适的标题请保留原文标题，若无，则设置一个合适的标题。
12. 章节编号请使用阿拉伯数字，请使用小数点'.'作为编号间隔符，请严格遵循上下文的编号，如上一段为 '# 3. '时，其子章节为 '# 3.2. '
13. 请严格保证章节编号是正确的、递增的、层次的，请正确，准确的设置章节编号，请确保每个段落都有编号。

***

以下是要进行转换格式的文本：

***

{query}

***

以上是要进行转换格式的文本。请根据要求，完成格式转换。

***

请帮我修改内容格式，我会给你一个PDF文档，文档中的文本可能是文字段落也可能来自表格。请将这些内容转换为markdown格式源码，且输出只有markdown源码，其他要求如下：
1. 无需考虑图片，只提取文字和表格
2. 要求格式为，PDF文本中的每一章节都作为markdown中的一个一级标题(只用一个 # 号)章节，无论章节还是子章节的标题，都要用markdown的一级标题表示，我们将用章节的编号来标记章节的级别。该章节的内容从这一章节的标题的后一行开始写。
3. 重点是准确识别文本中的章节编号和表格，表格格式请仔细处理。
4. 关于章节和编号，对于PDF中的一切章节，子章节，都要在markdown中对应一个一级标题章节（一个# 章节）并且用章节的编号来表示级别，而非多个#，章节编号均为"x.x.x. XXXX"的格式
5. 关于表格，一旦遇你认为是表格，请处理成如下格式，表格内容用markdown的格式源码，但前后不要换行：
---table begin---
Table tile: Name of Table
| column0 | column1 | column2 |
|---|---|---|
| row1 | value | value |
| row2 | value | value |
---table end---
说明：表格的前后由"---table begin---"和"---table end---"包裹，"---table begin---"的下一行是表名。
在提供的文本中，表格会被处理成每个cell一行，当你发现内容是表格时，请重新将其排列为markdown的表格格式。
此外，表格所在的段落也应有独立的标题。
6. 转换后的每个章节中只能有一个表格，如果有多段表格，请为每一个表格设置一个新章节，放置这个表格，并且设置合适的标题。
7. 输出内容只包含markdown源码，不要输出任何其他内容。markdown源码前后不要有说明和补充。
8. 你是一个支持超长文本的模型，你的任务是格式处理，因此不要省略、总结、丢弃任何内容，只要是输入的内容，也包括表格内容，都要在输出中体现出来。
9. 不要带 '```', 'markdown' 这种多余内容
10. 请谨慎使用 '#' 符号，这代表后面是一个独立章节的编号和标题。请正确，准确的使用'#'号设置章节。这一章节的内容从标题的后一行开始写。
11. 请为每个章节设置一个准确、简要的标题。如果原文中有合适的标题请保留原文标题，若无，则设置一个合适的标题。
12. 章节编号请使用阿拉伯数字，请使用小数点'.'作为编号间隔符，请严格遵循上下文的编号，如上一段为 '# 3. '时，其子章节为 '# 3.2. '
13. 请严格保证章节编号是正确的、递增的、层次的，请正确，准确的设置章节编号，请确保每个段落都有编号。
"""
    return prompt


def parse_markdown(file_content):
    file_content = file_content.replace('---table end---#', '---table end---\n\n#')
    lines = file_content.strip().split('\n')
    sections = []
    current_section = []

    for line in lines:
        while line.__contains__('##'):
            line = line.replace('##', '#')
        line = line.replace('```', '')
        line = line.replace('markdown', '')
        if line.startswith("# "):

            # Save the current section if not empty
            if current_section:
                section_text = "\n".join(current_section)
                if len(current_section) > 1:
                    # solve if this section contains more than one table
                    section_title = current_section[0]
                    # a table is defined by '---table begin---' and '---table end---'
                    # if a section contains more than one table, split it
                    if section_text.count('---table begin---') > 1:
                        split_tables = []
                        section_text = section_text.replace('---table end---', '---table end---\n')
                        section_text = section_text.replace('---table begin---', '\n---table begin---')
                        section_lines = section_text.split('\n')[1:]
                        table_content = section_title
                        for section_line in section_lines:
                            if section_line == '':
                                continue
                            if section_line == '---table end---':
                                table_content += '\n' + section_line
                                split_tables.append(table_content)
                                table_content = section_title
                            else:
                                table_content += '\n' + section_line
                        split_tables[-1] += '\n' + table_content
                        sections.extend(split_tables)
                    else:
                        sections.append(section_text)
                else:
                    sections.append(section_text)
                current_section.clear()
            current_section = [line]
            # # Determine hierarchy level
            # hierarchy_info = line[2:].split(".")
            # level = len(hierarchy_info)-1  # Level is determined by the number of dot-separated numbers
            # # Update hierarchy based on current level
            # if level <= len(hierarchy):
            #     hierarchy = hierarchy[:level-1]
            # hierarchy.append(hierarchy_info[-1].strip())
            # desc = "[desc] " + doc_title + " __ " + " __ ".join(hierarchy) + " [desc]"
            # current_section.append(desc)
        else:
            if line == '```':
                continue
            if len(line.strip()) > 0:
                current_section.append(line)

    # Save the last section if not empty
    # if current_section:
    #     sections.append("\n".join(current_section))

    return sections


def pdf2md(file_name):
    file_path = os.path.join('pdfs', file_name + '.pdf')
    text = extract_text_from_pdf(file_path)

    text_len = len(text)
    text_list = []

    # sliding window size and overlap
    chunk_size = 3000
    tolerance = 300
    for i in range(0, text_len, chunk_size):
        text_list.append(text[max(i-tolerance, 0):min(i + chunk_size + tolerance, text_len)])

    full_contents = {}
    history_prompt = None
    history_content = None
    title_chunk = False
    full_results = ''
    for chunk in tqdm.tqdm(text_list):
        # modify this if you need to fit your pdf format
        prompt = get_message(chunk)
        if history_content:
            if 2*tolerance > len(history_prompt):
                history_prompt = history_prompt
            else:
                history_prompt = history_prompt[-2*tolerance:]
            if 2*tolerance > len(history_content):
                history_content = history_content
            else:
                history_content = history_content[-2*tolerance:]
            message = [
                {"role": "system",
                 "content": """你是一个格式转换工具，根据要求转换文本的内容格式，用markdown输出转换后的内容，输出前后不要任何解释说明和标识。格式转换后不丢失原文内容。"""},
                {"role": "user", "content": history_prompt},
                {"role": "assistant", "content": history_content},
                {"role": "user", "content": "请参考前面转换好的文本，接着进行转换。\n" + prompt + "\n请参考历史记录中的文本，接着进行转换。"}
            ]
        else:
            message = [
                {"role": "system",
                 "content": """你是一个格式转换工具，根据要求转换文本的内容格式，用markdown输出转换后的内容，输出前后不要任何解释说明和标识。格式转换后不丢失原文内容。"""},
                {"role": "user", "content": prompt}
            ]

        # gpt-4-32k works better than preview version in terms of understanding instruction
        result = openai.ChatCompletion.create(
            # model="gpt-3.5-turbo-16k",
            # model='gpt-4-32k',
            model='gpt-4-turbo-preview',
            # max_tokens=4000,
            messages=message,

            stream=False
        )['choices'][0]['message']['content']
        if not title_chunk:
            result = '# ' + file_name + '\n\n' + result
            title_chunk = True

        full_results += result
        history_content = result
        history_prompt = prompt

    sections = parse_markdown(full_results)
    # last_contents = {}
    for section in sections:
        full_contents[section.split('\n')[0]] = section
        # last_contents[section.split('\n')[0]] = section
    # history_content = ''
    # for key, value in last_contents.items():
    #     history_content += value + '\n\n'

    full_markdown = ''
    for key, value in full_contents.items():
        full_markdown += value + '\n\n'

    with open(os.path.join('mds', file_name + '.md'), 'w', encoding='utf-8') as f:
        f.write(full_markdown)
    return full_markdown


# running pdf2md to convert a pdf file to a well-structured markdown
if __name__ == '__main__':
    start_time = time.time()
    md = pdf2md('adc12dj5200se')
    # # save to local
    # with open('test.md', 'w', encoding='utf-8') as f:
    #     f.write(md)
    print(time.time() - start_time)



