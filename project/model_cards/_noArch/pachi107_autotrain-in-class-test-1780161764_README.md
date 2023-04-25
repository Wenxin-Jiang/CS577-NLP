---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- pachi107/autotrain-data-in-class-test
co2_eq_emissions:
  emissions: 3.1621916284030838
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1780161764
- CO2 Emissions (in grams): 3.1622

## Validation Metrics

- Loss: 0.044
- Accuracy: 0.974
- Precision: 1.000
- Recall: 0.930
- AUC: 1.000
- F1: 0.964

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