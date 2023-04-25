---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- kyle-lucke/autotrain-data-planes
co2_eq_emissions:
  emissions: 0.19811345350195664
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1918465011
- CO2 Emissions (in grams): 0.1981

## Validation Metrics

- Loss: 0.011
- Accuracy: 0.997
- Macro F1: 0.916
- Micro F1: 0.997
- Weighted F1: 0.996
- Macro Precision: 0.999
- Micro Precision: 0.997
- Weighted Precision: 0.997
- Macro Recall: 0.867
- Micro Recall: 0.997
- Weighted Recall: 0.997

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