# Keyword Search

A keyword search package for CSV/Excel/Pandas using boolean expressions.

- It works by processing a query string with field indicator for Pandas Dataframe
columns. 

- Currently, only `.str.contains` queries are performed. 

- Boolean operations (`and`, `or`, `not`) are mantained during compilation. 

- All further work is done by the Pandas `DataFrame.query` method.


Searched field should not contain spaces or `:`.

*Examples:*

`((title:leptospira) and (abstract:vaccine))`

## Installation

```
$ pip install keyword-search
```

## Using as a Python package

```python
from keyword_search.query import keyword_search

df_results = keyword_search(df, "(title:Leptospirosis)")
print(df_results)
```

## Using as a CLI application

```
$ keyword-query papers.csv "(title:leptospira) or (abstract:leptospira)" --delimiter ";" --output results.csv
```