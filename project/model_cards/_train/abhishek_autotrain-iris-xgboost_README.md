---
tags:
- autotrain
- tabular
- classification
- tabular-classification
datasets:
- abhishek/autotrain-data-iris-train
- scikit-learn/iris
co2_eq_emissions: 1.9138035947108896
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 9705278
- CO2 Emissions (in grams): 1.9138035947108896

## Validation Metrics

- Loss: 0.2559724063922962
- Accuracy: 0.8666666666666667
- Macro F1: 0.8666666666666668
- Micro F1: 0.8666666666666667
- Weighted F1: 0.8666666666666667
- Macro Precision: 0.8666666666666667
- Micro Precision: 0.8666666666666667
- Weighted Precision: 0.8666666666666667
- Macro Recall: 0.8666666666666667
- Micro Recall: 0.8666666666666667
- Weighted Recall: 0.8666666666666667

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