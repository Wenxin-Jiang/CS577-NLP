---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- fyhao/autotrain-data-sentiment-analysis
co2_eq_emissions:
  emissions: 0.0803280731181239
widget:
  structuredData:
    text:
      - I am happy
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2435575634
- CO2 Emissions (in grams): 0.0803

## Validation Metrics

- Loss: 0.186
- Accuracy: 0.873
- Macro F1: 0.870
- Micro F1: 0.873
- Weighted F1: 0.868
- Macro Precision: 0.938
- Micro Precision: 0.873
- Weighted Precision: 0.896
- Macro Recall: 0.833
- Micro Recall: 0.873
- Weighted Recall: 0.873

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