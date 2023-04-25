---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Ahmed-Abousetta/autotrain-data-abunawaf-user
co2_eq_emissions:
  emissions: 0.6436453501778651
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1860163583
- CO2 Emissions (in grams): 0.6436

## Validation Metrics

- Loss: 0.344
- Accuracy: 0.869
- Precision: 0.698
- Recall: 0.612
- AUC: 0.856
- F1: 0.652

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-user-1860163583
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-user-1860163583", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-user-1860163583", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```