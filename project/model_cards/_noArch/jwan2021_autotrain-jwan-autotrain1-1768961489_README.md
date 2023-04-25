---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- jwan2021/autotrain-data-jwan-autotrain1
co2_eq_emissions:
  emissions: 2.9876405883375106
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1768961489
- CO2 Emissions (in grams): 2.9876

## Validation Metrics

- Loss: 0.042
- Accuracy: 0.983
- Precision: 1.000
- Recall: 0.953
- AUC: 1.000
- F1: 0.976

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