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
  emissions: 1.58506390711431
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1860163587
- CO2 Emissions (in grams): 1.5851

## Validation Metrics

- Loss: 0.339
- Accuracy: 0.878
- Precision: 0.702
- Recall: 0.673
- AUC: 0.852
- F1: 0.688

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-user-1860163587
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-user-1860163587", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-user-1860163587", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```