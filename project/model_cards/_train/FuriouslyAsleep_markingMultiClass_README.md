---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- FuriouslyAsleep/autotrain-data-markingClassifier
co2_eq_emissions: 0.5712537632313806
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 661319476
- CO2 Emissions (in grams): 0.5712537632313806

## Validation Metrics

- Loss: 0.859619140625
- Accuracy: 0.8
- Macro F1: 0.6
- Micro F1: 0.8000000000000002
- Weighted F1: 0.72
- Macro Precision: 0.5555555555555555
- Micro Precision: 0.8
- Weighted Precision: 0.6666666666666666
- Macro Recall: 0.6666666666666666
- Micro Recall: 0.8
- Weighted Recall: 0.8


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/FuriouslyAsleep/autonlp-markingClassifier-661319476
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("FuriouslyAsleep/autonlp-markingClassifier-661319476", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("FuriouslyAsleep/autonlp-markingClassifier-661319476", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```