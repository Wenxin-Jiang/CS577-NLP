---
tags:
- tabular-classification
- sklearn
datasets:
- wine-quality
- lvwerra/red-wine
widget:
  structuredData:
    fixed_acidity:
      - 7.4
      - 7.8
      - 10.3
    volatile_acidity:
      - 0.7
      - 0.88
      - 0.32
    citric_acid:
      - 0
      - 0
      - 0.45
    residual_sugar:
      - 1.9
      - 2.6
      - 6.4
    chlorides:
      - 0.076
      - 0.098
      - 0.073
    free_sulfur_dioxide:
      - 11
      - 25
      - 5
    total_sulfur_dioxide:
      - 34
      - 67
      - 13
    density:
      - 0.9978
      - 0.9968
      - 0.9976
    pH:
      - 3.51
      - 3.2
      - 3.23
    sulphates:
      - 0.56
      - 0.68
      - 0.82
    alcohol:
      - 9.4
      - 9.8
      - 12.6
---

## Wine Quality classification

### A Simple Example of Scikit-learn Pipeline

> Inspired by https://towardsdatascience.com/a-simple-example-of-pipeline-in-machine-learning-with-scikit-learn-e726ffbb6976 by Saptashwa Bhattacharyya


### How to use

```python
from huggingface_hub import hf_hub_url, cached_download
import joblib
import pandas as pd

REPO_ID = "julien-c/wine-quality"
FILENAME = "sklearn_model.joblib"


model = joblib.load(cached_download(
    hf_hub_url(REPO_ID, FILENAME)
))

# model is a `sklearn.pipeline.Pipeline`
```

#### Get sample data from this repo

```python
data_file = cached_download(
    hf_hub_url(REPO_ID, "winequality-red.csv")
)
winedf = pd.read_csv(data_file, sep=";")


X = winedf.drop(["quality"], axis=1)
Y = winedf["quality"]

print(X[:3])
```

|    |   fixed acidity |   volatile acidity |   citric acid |   residual sugar |   chlorides |   free sulfur dioxide |   total sulfur dioxide |   density |   pH |   sulphates |   alcohol |
|---:|----------------:|-------------------:|--------------:|-----------------:|------------:|----------------------:|-----------------------:|----------:|-----:|------------:|----------:|
|  0 |             7.4 |               0.7  |          0    |              1.9 |       0.076 |                    11 |                     34 |    0.9978 | 3.51 |        0.56 |       9.4 |
|  1 |             7.8 |               0.88 |          0    |              2.6 |       0.098 |                    25 |                     67 |    0.9968 | 3.2  |        0.68 |       9.8 |
|  2 |             7.8 |               0.76 |          0.04 |              2.3 |       0.092 |                    15 |                     54 |    0.997  | 3.26 |        0.65 |       9.8 |


#### Get your prediction

```python
labels = model.predict(X[:3])
# [5, 5, 5]
```

#### Eval

```python
model.score(X, Y)
# 0.6616635397123202
```

### 🍷 Disclaimer

No red wine was drunk (unfortunately) while training this model 🍷

