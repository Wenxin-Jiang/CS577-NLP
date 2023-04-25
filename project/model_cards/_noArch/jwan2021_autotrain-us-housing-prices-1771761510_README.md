---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- jwan2021/autotrain-data-us-housing-prices
co2_eq_emissions:
  emissions: 4.466856397835458
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1771761510
- CO2 Emissions (in grams): 4.4669

## Validation Metrics

- Loss: 102613.797
- R2: 0.919
- MSE: 10529591296.000
- MAE: 82375.211
- RMSLE: 0.100

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