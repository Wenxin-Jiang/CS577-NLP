---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- jwan2021/autotrain-data-us-housing-prices
co2_eq_emissions:
  emissions: 32.513983893680546
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1771761511
- CO2 Emissions (in grams): 32.5140

## Validation Metrics

- Loss: 134406.507
- R2: 0.861
- MSE: 18065109105.270
- MAE: 103271.843
- RMSLE: 0.139

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