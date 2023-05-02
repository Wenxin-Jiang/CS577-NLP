---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- abhishek/autotrain-data-adult-train
- scikit-learn/adult-census-income
co2_eq_emissions: 0.12693590577861977
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 9725286
- CO2 Emissions (in grams): 0.12693590577861977

## Validation Metrics

- Loss: 0.26716182056213406
- Accuracy: 0.8750191923844618
- Precision: 0.7840481565086531
- Recall: 0.6641172721478649
- AUC: 0.9345322809861784
- F1: 0.7191166321601105

## Usage

```python
import json
import joblib
import pandas as pd

model = joblib.load('model.joblib')
config = json.load(open('config.json'))

features = config['features']

# data = pd.read_csv("data.csv")
data = data[features]
data.columns = ["feat_" + str(col) for col in data.columns]

predictions = model.predict(data)  # or model.predict_proba(data)

```