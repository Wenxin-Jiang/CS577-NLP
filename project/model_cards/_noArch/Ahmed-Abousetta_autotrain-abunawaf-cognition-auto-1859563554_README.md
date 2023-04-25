---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Ahmed-Abousetta/autotrain-data-abunawaf-cognition-auto
co2_eq_emissions:
  emissions: 1.1747519267416993
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1859563554
- CO2 Emissions (in grams): 1.1748

## Validation Metrics

- Loss: 0.455
- Accuracy: 0.813
- Precision: 0.722
- Recall: 0.892
- AUC: 0.872
- F1: 0.798

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-cognition-auto-1859563554
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-auto-1859563554", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-auto-1859563554", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```