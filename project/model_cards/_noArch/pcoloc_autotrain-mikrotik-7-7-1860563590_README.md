---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- pcoloc/autotrain-data-mikrotik-7-7
co2_eq_emissions:
  emissions: 7.1011693391153115
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1860563590
- CO2 Emissions (in grams): 7.1012

## Validation Metrics

- Loss: 52.881
- R2: 0.584
- MSE: 2796.357
- MAE: 37.116
- RMSLE: 0.518

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