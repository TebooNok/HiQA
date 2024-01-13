# util.py
import os

def save_keywords(kb_name: str, keywords: list):
    from app import BASE_DIR
    directory = os.path.join(BASE_DIR, 'file_system', kb_name)
    file_path = os.path.join(directory, 'keywords.txt')

    with open(file_path, 'w', encoding='utf-8') as f:
        for keyword in keywords:
            f.write(keyword + '\n')


def load_keywords(kb_name: str):
    from app import BASE_DIR
    directory = os.path.join(BASE_DIR, 'file_system', kb_name)
    file_path = os.path.join(directory, 'keywords.txt')

    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]

def save_unkeywords(kb_name: str, keywords: list):
    from app import BASE_DIR
    directory = os.path.join(BASE_DIR, 'file_system', kb_name)
    file_path = os.path.join(directory, 'unkeywords.txt')

    with open(file_path, 'w', encoding='utf-8') as f:
        for keyword in keywords:
            f.write(keyword + '\n')

def load_unkeywords(kb_name: str):
    from app import BASE_DIR
    directory = os.path.join(BASE_DIR, 'file_system', kb_name)
    file_path = os.path.join(directory, 'unkeywords.txt')

    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]