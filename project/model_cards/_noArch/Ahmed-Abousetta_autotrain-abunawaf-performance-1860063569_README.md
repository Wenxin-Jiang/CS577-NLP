---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Ahmed-Abousetta/autotrain-data-abunawaf-performance
co2_eq_emissions:
  emissions: 0.6232110285492835
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1860063569
- CO2 Emissions (in grams): 0.6232

## Validation Metrics

- Loss: 0.430
- Accuracy: 0.841
- Precision: 0.846
- Recall: 0.825
- AUC: 0.873
- F1: 0.835

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-performance-1860063569
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-performance-1860063569", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-performance-1860063569", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```