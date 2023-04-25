---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- pcoloc/autotrain-data-dragino-7-7-max_300m
co2_eq_emissions:
  emissions: 0.12860686048945302
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1861063640
- CO2 Emissions (in grams): 0.1286

## Validation Metrics

- Loss: 50.918
- R2: 0.304
- MSE: 2592.667
- MAE: 39.693
- RMSLE: 0.429

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