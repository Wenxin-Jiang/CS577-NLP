---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- abhishek/autotrain-data-iris-train
- scikit-learn/iris
co2_eq_emissions: 0.15028701199056024
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 9705277
- CO2 Emissions (in grams): 0.15028701199056024

## Validation Metrics

- Loss: 0.15622713916762193
- Accuracy: 0.9
- Macro F1: 0.899749373433584
- Micro F1: 0.9
- Weighted F1: 0.8997493734335841
- Macro Precision: 0.9023569023569024
- Micro Precision: 0.9
- Weighted Precision: 0.9023569023569024
- Macro Recall: 0.9
- Micro Recall: 0.9
- Weighted Recall: 0.9

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