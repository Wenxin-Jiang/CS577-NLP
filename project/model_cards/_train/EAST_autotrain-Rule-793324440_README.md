---
tags: autotrain
language: zh
widget:
- text: "I love AutoTrain 🤗"
datasets:
- EAST/autotrain-data-Rule
co2_eq_emissions: 0.0025078722090032795
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 793324440
- CO2 Emissions (in grams): 0.0025078722090032795

## Validation Metrics

- Loss: 0.31105440855026245
- Accuracy: 0.9473684210526315
- Precision: 0.9
- Recall: 1.0
- AUC: 0.9444444444444445
- F1: 0.9473684210526316

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/EAST/autotrain-Rule-793324440
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("EAST/autotrain-Rule-793324440", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("EAST/autotrain-Rule-793324440", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```