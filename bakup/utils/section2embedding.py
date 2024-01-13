import openai
from dotenv import load_dotenv
import os
import tiktoken
import pandas as pd
from openai.embeddings_utils import get_embedding
from app import BASE_DIR
from service.config import settings

openai.api_key = settings.OPENAI_API_KEY
openai.api_base = settings.OPENAI_API_BASE

embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"

def split_and_embed(section, encoding,max_tokens=8000):
    # Get the title from the first line
    lines = section.split("\n")
    title = lines[0]
    content = "\n".join(lines[1:])

    half_length = len(content) // 2
    section_1 = title + "\n" + content[:half_length]
    section_2 = title + "\n" + content[half_length:]

    sections = [section_1, section_2]

    new_sections = []

    for sec in sections:
        if len(encoding.encode(sec)) > max_tokens:
            new_sections.extend(split_and_embed(sec, encoding))
        else:
            new_sections.append(sec)

    return new_sections

def section_to_embed(kb_name: str, file_name: str, max_tokens = 800):
    directory = os.path.join(BASE_DIR, 'file_system', kb_name, 'sections', file_name)
    name = os.path.splitext(file_name)[0]

    # embed_path = os.path.join(BASE_DIR, 'file_system', kb_name, 'embedded')
    df = pd.read_csv(directory, encoding='utf-8')
    encoding = tiktoken.get_encoding(embedding_encoding)

    new_df_entries = []

    for _, row in df.iterrows():
        section = row['section']
        n_tokens = len(encoding.encode(section))

        if '---table begin---' in section:
            # Get the content before and after the table as well as the table's title, column names, and row names
            table_start_idx = section.find('---table begin---')
            table_end_idx = section.find('---table end---') + len('---table end---')

            # Get the metadata before the table
            pre_table_content = section[:table_start_idx]

            # Get the table title
            table_title_start = table_start_idx + len('---table begin---')
            table_title_line = section[table_title_start:section.find('\n', table_title_start+1)].replace('Table title:', '').replace('Table tile:', '').strip()

            # print('title:', table_title_line)
            # Extract the table content and split into lines
            table_content = section[table_start_idx + len('---table begin---'):table_end_idx].split('\n')[1:-1]
            # print(table_content)
            # Get the table headers (column names)
            try:
                table_headers = table_content[1].strip().split('|')[1:-1] # Exclude the first and last empty items
            except IndexError as e:
                # print(section.find('---table begin---'), section.find('---table end---'))
                # print(section + '\n----sec---\n')
                continue
            # print(table_headers)
            table_headers = [header.strip() for header in table_headers]
            # print(table_headers)
            # Get the row names (assuming they are in the first column)
            table_row_names = []
            for row_content in table_content[3:]:
                if row_content[0] == '|':
                    table_row_names.append(row_content.split('|')[1].strip())
            # Embed metadata content
            metadata_content = '\n'.join([pre_table_content, table_title_line] + table_headers + table_row_names)
            # print('\n-------TABLE FOUND--------\n content:\n'+section+'\n metadata:\n'+metadata_content+'\n--------------------------\n')

            actual_section = section.replace('---table begin---', '').replace('---table end---', '')
            new_df_entries.append({'section': actual_section, 'n_tokens': len(encoding.encode(metadata_content)), 'embedding': get_embedding(metadata_content, engine=embedding_model)})

        else:
            if n_tokens < max_tokens:
                new_df_entries.append({'section': section, 'n_tokens': n_tokens, 'embedding': get_embedding(section, engine=embedding_model)})
            else:
                for new_section in split_and_embed(section, encoding):
                    new_df_entries.append({'section': new_section, 'n_tokens': len(encoding.encode(new_section)), 'embedding': get_embedding(new_section, engine=embedding_model)})

    df_new = pd.DataFrame(new_df_entries)

    embd_path = os.path.join(BASE_DIR, 'file_system', kb_name, 'embedded', file_name)
    df_new.to_csv(embd_path, index=False, encoding='utf-8')