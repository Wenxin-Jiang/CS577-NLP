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
  emissions: 3.157823361506444
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1859563557
- CO2 Emissions (in grams): 3.1578

## Validation Metrics

- Loss: 0.420
- Accuracy: 0.833
- Precision: 0.790
- Recall: 0.814
- AUC: 0.894
- F1: 0.802

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-cognition-auto-1859563557
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-auto-1859563557", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-auto-1859563557", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```