from nltk.stem import RSLPStemmer

st = RSLPStemmer()


def normalize_token(token):
    token = token.lower()
    return st.stem(token)
