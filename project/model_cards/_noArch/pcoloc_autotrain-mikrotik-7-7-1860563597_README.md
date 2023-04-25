---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- pcoloc/autotrain-data-mikrotik-7-7
co2_eq_emissions:
  emissions: 1.3260818006120507
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1860563597
- CO2 Emissions (in grams): 1.3261

## Validation Metrics

- Loss: 49.757
- R2: 0.632
- MSE: 2475.747
- MAE: 33.327
- RMSLE: 0.587

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