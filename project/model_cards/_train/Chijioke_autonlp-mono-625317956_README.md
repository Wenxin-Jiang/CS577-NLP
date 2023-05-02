---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Chijioke/autonlp-data-mono
co2_eq_emissions: 1.1406456838043837
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 625317956
- CO2 Emissions (in grams): 1.1406456838043837

## Validation Metrics

- Loss: 0.513037919998169
- Accuracy: 0.8982035928143712
- Macro F1: 0.7843756230226546
- Micro F1: 0.8982035928143712
- Weighted F1: 0.8891653474608059
- Macro Precision: 0.8210878091622635
- Micro Precision: 0.8982035928143712
- Weighted Precision: 0.8888857327766032
- Macro Recall: 0.7731018645485747
- Micro Recall: 0.8982035928143712
- Weighted Recall: 0.8982035928143712


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Chijioke/autonlp-mono-625317956
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Chijioke/autonlp-mono-625317956", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Chijioke/autonlp-mono-625317956", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```