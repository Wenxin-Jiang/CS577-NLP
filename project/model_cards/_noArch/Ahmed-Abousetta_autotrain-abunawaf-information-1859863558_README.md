---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Ahmed-Abousetta/autotrain-data-abunawaf-information
co2_eq_emissions:
  emissions: 0.7147232414393694
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1859863558
- CO2 Emissions (in grams): 0.7147

## Validation Metrics

- Loss: 0.354
- Accuracy: 0.865
- Precision: 0.817
- Recall: 0.887
- AUC: 0.931
- F1: 0.851

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-information-1859863558
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-information-1859863558", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-information-1859863558", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```