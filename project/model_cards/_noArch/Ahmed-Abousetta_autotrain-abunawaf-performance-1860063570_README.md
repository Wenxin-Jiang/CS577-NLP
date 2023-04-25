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
  emissions: 0.9744207053095343
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1860063570
- CO2 Emissions (in grams): 0.9744

## Validation Metrics

- Loss: 0.435
- Accuracy: 0.824
- Precision: 0.853
- Recall: 0.775
- AUC: 0.885
- F1: 0.812

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-performance-1860063570
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-performance-1860063570", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-performance-1860063570", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```