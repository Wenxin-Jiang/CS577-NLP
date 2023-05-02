---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Monsia/autonlp-data-tweets-classification
co2_eq_emissions: 4.819872182577655
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 23044997
- CO2 Emissions (in grams): 4.819872182577655

## Validation Metrics

- Loss: 0.001594889909029007
- Accuracy: 0.9997478885667465
- Macro F1: 0.9991190902836993
- Micro F1: 0.9997478885667465
- Weighted F1: 0.9997476735518704
- Macro Precision: 0.9998014460161265
- Micro Precision: 0.9997478885667465
- Weighted Precision: 0.9997479944069787
- Macro Recall: 0.9984426545713851
- Micro Recall: 0.9997478885667465
- Weighted Recall: 0.9997478885667465


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Monsia/autonlp-tweets-classification-23044997
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Monsia/autonlp-tweets-classification-23044997", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Monsia/autonlp-tweets-classification-23044997", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```