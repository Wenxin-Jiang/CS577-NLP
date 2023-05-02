---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Ajay191191/autonlp-data-Test
co2_eq_emissions: 55.10196329868386
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 530014983
- CO2 Emissions (in grams): 55.10196329868386

## Validation Metrics

- Loss: 0.23171618580818176
- Accuracy: 0.9298837645294338
- Precision: 0.9314414866901055
- Recall: 0.9279459594696022
- AUC: 0.979447403984557
- F1: 0.9296904373981703

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Ajay191191/autonlp-Test-530014983
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ajay191191/autonlp-Test-530014983", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ajay191191/autonlp-Test-530014983", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```