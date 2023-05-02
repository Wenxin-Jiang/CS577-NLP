---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- abhishek/autonlp-data-fred2
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 2682064

## Validation Metrics

- Loss: 0.4454168379306793
- Accuracy: 0.8188976377952756
- Precision: 0.8442028985507246
- Recall: 0.7103658536585366
- AUC: 0.8699702146791053
- F1: 0.771523178807947

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-fred2-2682064
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-fred2-2682064", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-fred2-2682064", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```