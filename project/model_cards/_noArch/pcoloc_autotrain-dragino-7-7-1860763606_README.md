---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- pcoloc/autotrain-data-dragino-7-7
co2_eq_emissions:
  emissions: 0.0005889255577470637
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1860763606
- CO2 Emissions (in grams): 0.0006

## Validation Metrics

- Loss: 84.433
- R2: 0.540
- MSE: 7129.004
- MAE: 62.626
- RMSLE: 0.418

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