---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- omarques/autotrain-data-in-class-test-demo
co2_eq_emissions:
  emissions: 0.15031698776128047
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1659958767
- CO2 Emissions (in grams): 0.1503

## Validation Metrics

- Loss: 0.076
- Accuracy: 0.983
- Precision: 1.000
- Recall: 0.953
- AUC: 0.999
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