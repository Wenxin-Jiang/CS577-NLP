---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- pediberto/autonlp-data-testing
co2_eq_emissions: 12.994518654810642
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 504313966
- CO2 Emissions (in grams): 12.994518654810642

## Validation Metrics

- Loss: 0.19673296809196472
- Accuracy: 0.9398032027783138
- Precision: 0.9133115705476967
- Recall: 0.9718255499807025
- AUC: 0.985316873222122
- F1: 0.9416604338070308

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/pediberto/autonlp-testing-504313966
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("pediberto/autonlp-testing-504313966", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("pediberto/autonlp-testing-504313966", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```