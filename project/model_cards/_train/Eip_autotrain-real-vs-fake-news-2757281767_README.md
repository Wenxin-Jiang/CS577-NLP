---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Eip/autotrain-data-real-vs-fake-news
co2_eq_emissions:
  emissions: 2.0552688377356976
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2757281767
- CO2 Emissions (in grams): 2.0553

## Validation Metrics

- Loss: 0.002
- Accuracy: 1.000
- Precision: 1.000
- Recall: 1.000
- AUC: 1.000
- F1: 1.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Eip/autotrain-real-vs-fake-news-2757281767
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Eip/autotrain-real-vs-fake-news-2757281767", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Eip/autotrain-real-vs-fake-news-2757281767", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```