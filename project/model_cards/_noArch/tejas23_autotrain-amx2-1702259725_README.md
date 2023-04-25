---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- tejas23/autotrain-data-amx2
co2_eq_emissions:
  emissions: 7.7048287301375975
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1702259725
- CO2 Emissions (in grams): 7.7048

## Validation Metrics

- Loss: 0.421
- Accuracy: 0.827
- Macro F1: 0.530
- Micro F1: 0.827
- Weighted F1: 0.805
- Macro Precision: 0.579
- Micro Precision: 0.827
- Weighted Precision: 0.795
- Macro Recall: 0.513
- Micro Recall: 0.827
- Weighted Recall: 0.827

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