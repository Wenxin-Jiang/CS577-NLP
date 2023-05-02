---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Fauzan/autonlp-data-judulberita
co2_eq_emissions: 0.9413042739759596
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 32517788
- CO2 Emissions (in grams): 0.9413042739759596

## Validation Metrics

- Loss: 0.32112351059913635
- Accuracy: 0.8641304347826086
- Precision: 0.8055555555555556
- Recall: 0.8405797101449275
- AUC: 0.9493383742911153
- F1: 0.8226950354609929

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Fauzan/autonlp-judulberita-32517788
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Fauzan/autonlp-judulberita-32517788", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Fauzan/autonlp-judulberita-32517788", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```