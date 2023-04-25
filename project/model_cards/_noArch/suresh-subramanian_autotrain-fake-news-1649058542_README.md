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
  emissions: 12.699762619910537
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1649058542
- CO2 Emissions (in grams): 12.6998

## Validation Metrics

- Loss: 0.624
- Accuracy: 0.637
- Precision: 1.000
- Recall: 0.020
- AUC: 0.652
- F1: 0.039

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/suresh-subramanian/autotrain-fake-news-1649058542
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("suresh-subramanian/autotrain-fake-news-1649058542", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("suresh-subramanian/autotrain-fake-news-1649058542", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```