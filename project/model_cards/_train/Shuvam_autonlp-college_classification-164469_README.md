---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Shuvam/autonlp-data-college_classification
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 164469

## Validation Metrics

- Loss: 0.05527503043413162
- Accuracy: 0.9853049228508449
- Precision: 0.991044776119403
- Recall: 0.9793510324483776
- AUC: 0.9966895139869654
- F1: 0.9851632047477745

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Shuvam/autonlp-college_classification-164469
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Shuvam/autonlp-college_classification-164469", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Shuvam/autonlp-college_classification-164469", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```