# 只需要有一个get_embedding的函数就可以了，输入一个文本，输出其向量

import openai
import os
import tiktoken
import pandas as pd
from openai.embeddings_utils import get_embedding

os.environ["OPENAI_API_KEY"] = "yPKz6gw9KNVZd6oBFQ2AoZvosF3TvX6C3XJbADgahZYj3wZNHNuhRMoDG9pzpN98"
os.environ["OPENAI_API_BASE"] = "https://ai.api.moblin.net/api/openai/v1"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")
embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"
max_tokens = 8000

def split_and_embed(section, encoding):
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

input_datapath = 'others_products_new.csv'
df = pd.read_csv(input_datapath, encoding='utf-8')
encoding = tiktoken.get_encoding(embedding_encoding)

new_df_entries = []

import tqdm
for _, row in tqdm.tqdm(df.iterrows()):
    section = row['section']
    n_tokens = len(encoding.encode(section))

    meta_content = '\n'.join(section.split("\n")[:4])
    new_df_entries.append({'section': section, 'n_tokens': n_tokens, 'embedding': get_embedding(meta_content, engine=embedding_model)})

df_new = pd.DataFrame(new_df_entries)
df_new.to_csv("竞品", index=False, encoding='utf-8')
