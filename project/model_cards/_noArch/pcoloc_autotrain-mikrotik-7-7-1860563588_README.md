---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- pcoloc/autotrain-data-mikrotik-7-7
co2_eq_emissions:
  emissions: 1.538605928853103
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1860563588
- CO2 Emissions (in grams): 1.5386

## Validation Metrics

- Loss: 48.213
- R2: 0.654
- MSE: 2324.518
- MAE: 32.634
- RMSLE: 0.586

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