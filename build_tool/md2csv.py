import os
import pandas as pd
import os.path


def parse_markdown(file_content):
    lines = file_content.strip().split('\n')
    sections = []
    current_section = []
    hierarchy = []

    doc_title = None
    for line in lines:
        if line.startswith("# "):
            if not doc_title:
                doc_title = line[2:].strip()
                continue

            # Save the current section if not empty
            if current_section:
                if len(current_section) == 1 and current_section[0].startswith("[desc]"):
                    current_section.clear()
                else:
                    sections.append("\n".join(current_section))
                    current_section.clear()

            # Determine hierarchy level
            hierarchy_info = line[2:].split(".")
            level = len(hierarchy_info) - 1  # Level is determined by the number of dot-separated numbers
            # Update hierarchy based on current level
            if level <= len(hierarchy):
                hierarchy = hierarchy[:level - 1]
            hierarchy.append(hierarchy_info[-1].strip())
            desc = "[desc] " + doc_title + " __ " + " __ ".join(hierarchy) + " [desc]"
            current_section.append(desc)
        else:
            if line == '...':
                continue
            if (len(line.strip()) > 0):
                current_section.append(line)

    # Save the last section if not empty
    if current_section:
        sections.append("\n".join(current_section))

    return doc_title, sections


def list_md_files(directory: str):
    """
    递归遍历给定目录下的所有.md文件，并返回它们的路径和不带.md扩展名的文件名。

    参数:
    - directory: 要遍历的目录路径

    返回:
    - 一个元组的列表，每个元组包含文件的完整路径和不带.md扩展名的文件名
    """
    md_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                file_name_without_extension = os.path.splitext(file)[0]
                md_files.append((full_path, file_name_without_extension))

    return md_files


def md2sections(file_name: str):
    name = os.path.splitext(file_name)[0]
    directory = os.path.join('sections')
    file_path = os.path.join('mds', file_name)

    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        title, sections = parse_markdown(file_content)
        df = pd.DataFrame(sections, columns=['section'])
        df.to_csv(directory + "/" + name + '.csv', index=False, encoding='utf-8')


# md2sections('卓胜微.md')
# md2sections('唯捷创芯.md')
# md2sections('思瑞浦.md')
# md2sections('艾为.md')
md2sections('南亚新材.md')
md2sections('广东生益.md')
md2sections('浙江华正.md')
md2sections('金安国记.md')
