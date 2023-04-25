---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Ahmed-Abousetta/autotrain-data-abunawaf-interaction
co2_eq_emissions:
  emissions: 0.7644156643824811
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1859963563
- CO2 Emissions (in grams): 0.7644

## Validation Metrics

- Loss: 0.244
- Accuracy: 0.910
- Precision: 0.935
- Recall: 0.935
- AUC: 0.954
- F1: 0.935

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-interaction-1859963563
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-interaction-1859963563", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-interaction-1859963563", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```