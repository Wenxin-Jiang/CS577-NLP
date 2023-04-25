---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- jwan2021/autotrain-data-us-housing-prices
co2_eq_emissions:
  emissions: 0.12978708384729631
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1771761513
- CO2 Emissions (in grams): 0.1298

## Validation Metrics

- Loss: 100581.032
- R2: 0.922
- MSE: 10116543945.030
- MAE: 81586.656
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