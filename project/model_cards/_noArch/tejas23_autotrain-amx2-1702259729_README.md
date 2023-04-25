---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- tejas23/autotrain-data-amx2
co2_eq_emissions:
  emissions: 0.002766545033914285
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1702259729
- CO2 Emissions (in grams): 0.0028

## Validation Metrics

- Loss: 6.095
- Accuracy: 0.824
- Macro F1: 0.543
- Micro F1: 0.824
- Weighted F1: 0.808
- Macro Precision: 0.572
- Micro Precision: 0.824
- Weighted Precision: 0.801
- Macro Recall: 0.543
- Micro Recall: 0.824
- Weighted Recall: 0.824

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