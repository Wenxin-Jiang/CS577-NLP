---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- pcoloc/autotrain-data-only-rssi
co2_eq_emissions:
  emissions: 1.3554114117578944
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1813762559
- CO2 Emissions (in grams): 1.3554

## Validation Metrics

- Loss: 83.432
- R2: 0.312
- MSE: 6960.888
- MAE: 60.449
- RMSLE: 0.532

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