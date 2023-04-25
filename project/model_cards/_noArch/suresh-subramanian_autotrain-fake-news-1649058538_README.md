---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- suresh-subramanian/autotrain-data-fake-news
co2_eq_emissions:
  emissions: 0.04097854185629584
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1649058538
- CO2 Emissions (in grams): 0.0410

## Validation Metrics

- Loss: 0.387
- Accuracy: 0.815
- Precision: 0.760
- Recall: 0.730
- AUC: 0.902
- F1: 0.745

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/suresh-subramanian/autotrain-fake-news-1649058538
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("suresh-subramanian/autotrain-fake-news-1649058538", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("suresh-subramanian/autotrain-fake-news-1649058538", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```