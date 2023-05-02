---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Someshfengde/autonlp-data-kaggledays
co2_eq_emissions: 28.622267513847273
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 625717992
- CO2 Emissions (in grams): 28.622267513847273

## Validation Metrics

- Loss: 0.8782362937927246
- Accuracy: 0.6022282660559214
- Macro F1: 0.6024258279848015
- Micro F1: 0.6022282660559214
- Weighted F1: 0.6024299908624371
- Macro Precision: 0.604093172183357
- Micro Precision: 0.6022282660559214
- Weighted Precision: 0.6041166306778806
- Macro Recall: 0.6022424576798522
- Micro Recall: 0.6022282660559214
- Weighted Recall: 0.6022282660559214


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Someshfengde/autonlp-kaggledays-625717992
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Someshfengde/autonlp-kaggledays-625717992", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Someshfengde/autonlp-kaggledays-625717992", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```