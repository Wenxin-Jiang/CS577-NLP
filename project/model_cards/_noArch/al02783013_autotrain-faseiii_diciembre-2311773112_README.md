---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- al02783013/autotrain-data-faseiii_diciembre
co2_eq_emissions:
  emissions: 4.041080293052415
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 2311773112
- CO2 Emissions (in grams): 4.0411

## Validation Metrics

- Loss: 5487.957
- R2: 0.960
- MSE: 30117668.000
- MAE: 2082.499
- RMSLE: 1.918

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