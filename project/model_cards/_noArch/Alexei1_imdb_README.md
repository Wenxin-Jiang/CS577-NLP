---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- Alexei1/autotrain-data-imdb-sentiment-analysis
co2_eq_emissions:
  emissions: 0.018564765189754893
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1530155186
- CO2 Emissions (in grams): 0.0186

## Validation Metrics

- Loss: 0.694
- Accuracy: 0.487
- Macro F1: 0.218
- Micro F1: 0.487
- Weighted F1: 0.319
- Macro Precision: 0.162
- Micro Precision: 0.487
- Weighted Precision: 0.237
- Macro Recall: 0.333
- Micro Recall: 0.487
- Weighted Recall: 0.487

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