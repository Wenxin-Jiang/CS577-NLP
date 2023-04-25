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
  emissions: 0.7623869342782728
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1859563556
- CO2 Emissions (in grams): 0.7624

## Validation Metrics

- Loss: 0.404
- Accuracy: 0.829
- Precision: 0.754
- Recall: 0.873
- AUC: 0.901
- F1: 0.809

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-cognition-auto-1859563556
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-auto-1859563556", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-auto-1859563556", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```