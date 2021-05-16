from se.tfidf import make_tfidf

def score_document(query, tfidf):
    score = 0
    for word in query:
        score += tfidf.get(word, 0)
    return score


def rank_documents(query_structure, docs, index_query):

    tfidf = make_tfidf(docs)
    ranked_index = []
    for doc_number in index_query:
        score = score_document(query_structure, tfidf[doc_number])
        ranked_index.append((score, doc_number))
    ranked_index = sorted(ranked_index, key=lambda x: -x[0])
    return [item[1] for item in ranked_index]
