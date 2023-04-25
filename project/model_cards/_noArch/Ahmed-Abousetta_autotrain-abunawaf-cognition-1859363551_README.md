---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Ahmed-Abousetta/autotrain-data-abunawaf-cognition
co2_eq_emissions:
  emissions: 1.7828199447393138
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1859363551
- CO2 Emissions (in grams): 1.7828

## Validation Metrics

- Loss: 0.372
- Accuracy: 0.858
- Precision: 0.796
- Recall: 0.882
- AUC: 0.919
- F1: 0.837

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-cognition-1859363551
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-1859363551", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-1859363551", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```