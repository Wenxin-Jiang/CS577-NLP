---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- abhishek/autonlp-data-toxic-new
co2_eq_emissions: 30.684995819386277
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 30516963
- CO2 Emissions (in grams): 30.684995819386277

## Validation Metrics

- Loss: 0.08340361714363098
- Accuracy: 0.9688222161294113
- Precision: 0.9102096627164995
- Recall: 0.7692604006163328
- AUC: 0.9859340458715813
- F1: 0.8338204592901879

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-toxic-new-30516963
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-toxic-new-30516963", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-toxic-new-30516963", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```