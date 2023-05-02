---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Jeska/autonlp-data-vaccinfaq
co2_eq_emissions: 27.135492487925884
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 22144706
- CO2 Emissions (in grams): 27.135492487925884

## Validation Metrics

- Loss: 1.81697416305542
- Accuracy: 0.6377269139700079
- Macro F1: 0.5181293370145044
- Micro F1: 0.6377269139700079
- Weighted F1: 0.631117826235572
- Macro Precision: 0.5371452512845428
- Micro Precision: 0.6377269139700079
- Weighted Precision: 0.6655055695465463
- Macro Recall: 0.5609328178925124
- Micro Recall: 0.6377269139700079
- Weighted Recall: 0.6377269139700079


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Jeska/autonlp-vaccinfaq-22144706
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Jeska/autonlp-vaccinfaq-22144706", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Jeska/autonlp-vaccinfaq-22144706", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```