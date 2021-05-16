# A low level search engine

## Install library localy

```
pip install -e .
```

## Download and extract kaggle dataset

https://www.kaggle.com/fogelman/brazilian-news

## Create archieve

```
python scripts/make_archive.py --input=data/news.csv --limit=1000
```

## Create index

```
python scripts/make_index_from_archive.py
```

## Search Documents

```
python scripts/search.py "governo or estado"
```
