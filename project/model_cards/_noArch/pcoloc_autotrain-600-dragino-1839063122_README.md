---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- pcoloc/autotrain-data-600-dragino
co2_eq_emissions:
  emissions: 0.12762962748859905
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1839063122
- CO2 Emissions (in grams): 0.1276

## Validation Metrics

- Loss: 93.595
- R2: 0.502
- MSE: 8760.052
- MAE: 77.527
- RMSLE: 0.445

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