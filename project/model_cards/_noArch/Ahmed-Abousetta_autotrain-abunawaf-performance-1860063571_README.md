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
  emissions: 0.6594479502465727
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1860063571
- CO2 Emissions (in grams): 0.6594

## Validation Metrics

- Loss: 0.447
- Accuracy: 0.824
- Precision: 0.841
- Recall: 0.792
- AUC: 0.886
- F1: 0.815

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-performance-1860063571
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-performance-1860063571", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-performance-1860063571", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```