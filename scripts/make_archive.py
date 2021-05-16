#!/usr/bin/env python3
import json

from argparse import ArgumentParser

import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm
from nltk.tokenize import word_tokenize


from se.archive import save_archive
from se.transform import filter_tokens

MSG_DESCRIPTION = '''Le arquivo de tweets e gera JSON com tweets tokenizados.
Tweets obtidos de https://www.kaggle.com/kingburrito666/better-donald-trump-tweets
'''


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tags = [tag.text for tag in soup.select("p")]

    if len(tags) > 1:
        tags = tags[1:]

    cleaned = "\n".join(tags)

    return cleaned


def tokenize_corpus(path, limit):
    
    df = pd.read_csv(path)
    documents = {}
    for row in tqdm(df.itertuples(index=False)):
        try:
            html = row.html
            _id = row.id

            document = parse_html(html)
            tokens = word_tokenize(document, language="portuguese")
            documents[_id] = filter_tokens(tokens)
        except:
            continue

        if limit is not None and (len(documents) >= limit):
            break

    return documents


def main():
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument('--input', help='News Dataset')
    parser.add_argument('--output', default="data/archive.json")
    parser.add_argument('--limit', type=int, default=None)

    args = parser.parse_args()

    docs = tokenize_corpus(args.input, args.limit)
    save_archive(docs, args.output)


if __name__ == '__main__':
    main()
