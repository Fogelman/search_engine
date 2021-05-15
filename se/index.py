import json

from collections import defaultdict


def make_index(docs):
    index = defaultdict(list)
    for k, doc in docs.items():
        words = set(doc)
        for word in words:
            index[word].append(k)
    return index


def save_index(index, path):
    with open(path, 'w', encoding="utf-8") as file:
        json.dump(index, file, indent=4)


def load_index(path):
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)
