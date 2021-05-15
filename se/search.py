from se.query import parse_raw_query
from se.retrieve import retrieve
from se.rank import rank_documents

def search(raw_query, index, docs):
    query = parse_raw_query(raw_query)
    json_query = parse_json_query(query)

    idx = Index(index)

    index_query = json_query.evaluate(idx)

    terms = terms = extract_terms(raw_query)

    ranked_index = rank_documents(terms, docs, index_query)
    
    return [docs[k] for k in ranked_index]
