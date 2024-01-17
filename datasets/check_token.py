import tiktoken

embedding_encoding = "cl100k_base"
encoding = tiktoken.get_encoding(embedding_encoding)
# n_tokens = len(encoding.encode(role))
# print(n_tokens)

# load all csv in '1_Chipanalog/embeddings', count total row number, count total length of char, count totol tokens
import os
import pandas as pd
import tqdm
import numpy as np

total_row = 0
total_char = 0
total_tokens = 0
total_words = 0
for file in tqdm.tqdm(os.listdir('1_Chipanalog/embeddings')):
    df = pd.read_csv(os.path.join('1_Chipanalog/embeddings', file), encoding='utf-8')
    total_row += len(df)
    for _, row in df.iterrows():
        total_char += len(row['section'])
        total_words += len(row['section'].split(' '))
        total_tokens += len(encoding.encode(row['section']))

print('Chipanalog')
print('total row:', total_row)
print('total char:', total_char)
print('total tokens:', total_tokens)
print('total words:', total_words)


# similarly, print these count for '2_Analog_Book'
total_row = 0
total_char = 0
total_tokens = 0
total_words = 0

for file in tqdm.tqdm(os.listdir('2_Analog_Book/embeddings')):
    df = pd.read_csv(os.path.join('2_Analog_Book/embeddings', file), encoding='utf-8')
    total_row += len(df)
    for _, row in df.iterrows():
        total_char += len(row['section'])
        total_words += len(row['section'].split(' '))
        total_tokens += len(encoding.encode(row['section']))

print('Analog_Book')
print('total row:', total_row)
print('total char:', total_char)
print('total tokens:', total_tokens)
print('total words:', total_words)

# similarly, print these count for '3_Annual financial reports'
total_row = 0
total_char = 0
total_tokens = 0
total_words = 0

for file in tqdm.tqdm(os.listdir('3_Annual financial reports/embeddings')):
    df = pd.read_csv(os.path.join('3_Annual financial reports/embeddings', file), encoding='utf-8')
    total_row += len(df)
    for _, row in df.iterrows():
        total_char += len(row['section'])
        total_words += len(row['section'].split(' '))
        total_tokens += len(encoding.encode(row['section']))

print('Annual financial reports')
print('total row:', total_row)
print('total char:', total_char)
print('total tokens:', total_tokens)
print('total words:', total_words)

# similarly, print these count for '3_Annual financial reports'
total_row = 0
total_char = 0
total_tokens = 0
total_words = 0

for file in tqdm.tqdm(os.listdir('4_Texas Instruments/embeddings')):
    df = pd.read_csv(os.path.join('4_Texas Instruments/embeddings', file), encoding='utf-8')
    total_row += len(df)
    for _, row in df.iterrows():
        total_char += len(row['section'])
        total_words += len(row['section'].split(' '))
        total_tokens += len(encoding.encode(row['section']))

print('Texas Instruments')
print('total row:', total_row)
print('total char:', total_char)
print('total tokens:', total_tokens)
print('total words:', total_words)
