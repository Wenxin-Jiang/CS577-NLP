---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- Robertooo/autotrain-data-hmaet
co2_eq_emissions:
  emissions: 0.30327638531180195
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 2037366891
- CO2 Emissions (in grams): 0.3033

## Validation Metrics

- Loss: 0.067
- R2: 0.486
- MSE: 0.005
- MAE: 0.055
- RMSLE: 0.036

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