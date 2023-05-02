---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Qinghui/autonlp-data-fake-covid-news
co2_eq_emissions: 23.42719853096565
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 36769078
- CO2 Emissions (in grams): 23.42719853096565

## Validation Metrics

- Loss: 0.15959647297859192
- Accuracy: 0.9817757009345794
- Precision: 0.980411361410382
- Recall: 0.9813725490196078
- AUC: 0.9982379201680672
- F1: 0.9808917197452229

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Qinghui/autonlp-fake-covid-news-36769078
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Qinghui/autonlp-fake-covid-news-36769078", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Qinghui/autonlp-fake-covid-news-36769078", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```