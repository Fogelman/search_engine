# A low level search engine

## Install library localy

```
pip install -e .
```

## Download and extract kaggle dataset

https://www.kaggle.com/fogelman/brazilian-news

## Create archieve

```
python scripts/make_archive.py --input=news.csv --output=tokens.json --limit=10000
```

## Create index

```
python scripts/make_index_from_archieve.py tokens.json index.json
```
