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
  emissions: 1.0566666951225436
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1859363549
- CO2 Emissions (in grams): 1.0567

## Validation Metrics

- Loss: 0.385
- Accuracy: 0.854
- Precision: 0.795
- Recall: 0.873
- AUC: 0.900
- F1: 0.832

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-cognition-1859363549
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-1859363549", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-1859363549", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```