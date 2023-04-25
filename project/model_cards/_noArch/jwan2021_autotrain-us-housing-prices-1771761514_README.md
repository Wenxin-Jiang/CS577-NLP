---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- jwan2021/autotrain-data-us-housing-prices
co2_eq_emissions:
  emissions: 0.1288210176412382
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1771761514
- CO2 Emissions (in grams): 0.1288

## Validation Metrics

- Loss: 100595.980
- R2: 0.922
- MSE: 10119551129.473
- MAE: 81601.198
- RMSLE: 0.101

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