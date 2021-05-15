#!/usr/bin/env python3
import json

from argparse import ArgumentParser

import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm
from nltk.tokenize import word_tokenize


from se.archive import save_archive
from se.transform import normalize_token

MSG_DESCRIPTION = '''Le arquivo de tweets e gera JSON com tweets tokenizados.
Tweets obtidos de https://www.kaggle.com/kingburrito666/better-donald-trump-tweets
'''


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    cleaned = "\n".join([tag.text for tag in soup.select("p")[1:]])

    return cleaned


def tokenize_corpus(path, limit):
    df = pd.read_csv(path)
    documents = {}
    for row in df.itertuples(index=False):
        try:
            html = row.html
            _id = row.id

            document = parse_html(html)
            tokens = word_tokenize(document, language="portuguese")
            documents[_id] = list(map(normalize_token, tokens))
        except:
            continue

        if limit is not None and (len(documents) >= limit):
            break

    return documents


def main():
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument('--input', help='News Dataset')
    parser.add_argument('--output', help='Where the archieve is stored')
    parser.add_argument('--limit', type=int, default=None)

    args = parser.parse_args()

    docs = tokenize_corpus(args.input, args.limit)
    save_archive(docs, args.output)


if __name__ == '__main__':
    main()
