#!/usr/bin/env python3
from argparse import ArgumentParser

from se.archive import load_archive
from se.index import make_index, save_index


MSG_DESCRIPTION = 'Le docs e gera indice reverso.'


def main():
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument('--input', help='News Dataset')
    parser.add_argument('--output', help='Where the archieve is stored')
    args = parser.parse_args()

    docs = load_archive(args.input)
    index = make_index(docs)

    save_index(index, args.output)


if __name__ == '__main__':
    main()
