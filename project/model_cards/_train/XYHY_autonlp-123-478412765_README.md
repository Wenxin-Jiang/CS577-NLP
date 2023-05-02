---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- XYHY/autonlp-data-123
co2_eq_emissions: 69.86520391863117
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 478412765
- CO2 Emissions (in grams): 69.86520391863117

## Validation Metrics

- Loss: 0.186362624168396
- Accuracy: 0.9539955699437723
- Precision: 0.9527454242928453
- Recall: 0.9572049481778669
- AUC: 0.9903929997079495
- F1: 0.9549699799866577

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/XYHY/autonlp-123-478412765
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("XYHY/autonlp-123-478412765", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("XYHY/autonlp-123-478412765", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```