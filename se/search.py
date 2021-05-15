from se.query import parse_raw_query, parse_json_query
from se.rank import rank_documents

def extract_terms(raw_query):
    split_query = raw_query.split()
    return [split_query[i] for i in range(len(split_query)) if i % 2 == 0]

def search(raw_query, index, docs):
    query = parse_raw_query(raw_query)
    print(query[0])
    json_query = parse_json_query(query[0])

    index_query = json_query.evaluate(index)

    terms = terms = extract_terms(raw_query)

    ranked_index = rank_documents(terms, docs, index)

    return [docs[k] for k in ranked_index]
