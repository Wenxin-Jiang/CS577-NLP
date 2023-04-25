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
  emissions: 1.0555869183889894
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1859963567
- CO2 Emissions (in grams): 1.0556

## Validation Metrics

- Loss: 0.263
- Accuracy: 0.910
- Precision: 0.945
- Recall: 0.923
- AUC: 0.945
- F1: 0.934

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-interaction-1859963567
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-interaction-1859963567", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-interaction-1859963567", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```