---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- pcoloc/autotrain-data-dragino-7-7-max_495m
co2_eq_emissions:
  emissions: 0.011242326266844769
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1860863627
- CO2 Emissions (in grams): 0.0112

## Validation Metrics

- Loss: 72.730
- R2: 0.386
- MSE: 5289.600
- MAE: 60.230
- RMSLE: 0.436

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