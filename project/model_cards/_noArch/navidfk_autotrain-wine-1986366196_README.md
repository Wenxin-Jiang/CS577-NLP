---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- navidfk/autotrain-data-wine
co2_eq_emissions:
  emissions: 23.98337622177028
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1986366196
- CO2 Emissions (in grams): 23.9834

## Validation Metrics

- Loss: 0.792
- Accuracy: 0.705
- Macro F1: 0.345
- Micro F1: 0.705
- Weighted F1: 0.683
- Macro Precision: 0.365
- Micro Precision: 0.705
- Weighted Precision: 0.676
- Macro Recall: 0.341
- Micro Recall: 0.705
- Weighted Recall: 0.705

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