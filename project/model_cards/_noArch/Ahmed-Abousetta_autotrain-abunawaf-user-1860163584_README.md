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
  emissions: 1.0492185026433665
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1860163584
- CO2 Emissions (in grams): 1.0492

## Validation Metrics

- Loss: 0.340
- Accuracy: 0.890
- Precision: 0.712
- Recall: 0.755
- AUC: 0.901
- F1: 0.733

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-user-1860163584
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-user-1860163584", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-user-1860163584", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```