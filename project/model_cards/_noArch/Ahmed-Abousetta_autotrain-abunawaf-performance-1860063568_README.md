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
  emissions: 1.0292657249217085
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1860063568
- CO2 Emissions (in grams): 1.0293

## Validation Metrics

- Loss: 0.453
- Accuracy: 0.812
- Precision: 0.836
- Recall: 0.767
- AUC: 0.860
- F1: 0.800

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-performance-1860063568
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-performance-1860063568", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-performance-1860063568", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```