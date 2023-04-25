---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- kem000123/autotrain-data-model1-binary-class
co2_eq_emissions:
  emissions: 4.092983833698762
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1843363194
- CO2 Emissions (in grams): 4.0930

## Validation Metrics

- Loss: 0.036
- Accuracy: 1.000
- Precision: 1.000
- Recall: 1.000
- AUC: 1.000
- F1: 1.000

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