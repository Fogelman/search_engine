import json
import numpy as np
from collections import defaultdict, Counter

def make_tfidf(docs):
    tf_all = {}
    idf_all = Counter()
    for k, v in docs.items():
        n = len(v)
        counter = Counter(v)    
        
        tf = {}
        for term, count in counter.items():
            tf[term] = count/n
            
        tf_all[k] = tf
        idf_all.update(counter.keys())

    N = len(docs)

    tfidf = {}
    for k, v in docs.items():
        tf = tf_all[k]
        _abc = {}
        
        for term in tf:
            _abc[term] = tf[term] * np.log2(N/(idf_all[term] + 1))
        
        tfidf[k] = _abc
            
    return tfidf

def save_tfidf(index, path):
    with open(path, 'w', encoding="utf-8") as file:
        json.dump(index, file, indent=4)


def load_tfidf(path):
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)
