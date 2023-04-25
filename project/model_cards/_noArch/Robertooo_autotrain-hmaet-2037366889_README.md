---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- Robertooo/autotrain-data-hmaet
co2_eq_emissions:
  emissions: 0.04056452250649151
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 2037366889
- CO2 Emissions (in grams): 0.0406

## Validation Metrics

- Loss: 0.003
- R2: 0.999
- MSE: 0.000
- MAE: 0.001
- RMSLE: 0.002

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