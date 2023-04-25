---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- tejas23/autotrain-data-amx2
co2_eq_emissions:
  emissions: 0.00824689737605251
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1702259728
- CO2 Emissions (in grams): 0.0082

## Validation Metrics

- Loss: 0.434
- Accuracy: 0.831
- Macro F1: 0.521
- Micro F1: 0.831
- Weighted F1: 0.803
- Macro Precision: 0.590
- Micro Precision: 0.831
- Weighted Precision: 0.794
- Macro Recall: 0.507
- Micro Recall: 0.831
- Weighted Recall: 0.831

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