---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- jwan2021/autotrain-data-us-housing-prices
co2_eq_emissions:
  emissions: 50.53686341531619
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1771761512
- CO2 Emissions (in grams): 50.5369

## Validation Metrics

- Loss: 122809.223
- R2: 0.884
- MSE: 15082105200.447
- MAE: 95586.887
- RMSLE: 0.130

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