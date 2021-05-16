#!/usr/bin/env python3
from argparse import ArgumentParser

from se.archive import load_archive
from se.index import load_index
from se.search import search


MSG_DESCRIPTION = 'Busca.'


def main():
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument('query', nargs='+', help='A query.')
    parser.add_argument('--filename_docs', default="data/archive.json")
    parser.add_argument('--filename_index', default="data/index.json")
    parser.add_argument('--limit', type=int, default=50)
    args = parser.parse_args()

    docs = load_archive(args.filename_docs)
    index = load_index(args.filename_index)

    docs_searched = search(' '.join(args.query), index, docs)

    limit = args.limit
    if limit > 0 and len(docs_searched) > limit:
        docs_searched = docs_searched[:limit]
    for doc in docs_searched:
        _id = doc.split("-")[0]
        print(f"https://www2.senado.leg.br/bdsf/handle/id/{_id}")
        print('=' * 80)


if __name__ == '__main__':
    main()
