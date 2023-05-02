---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Someshfengde/autonlp-data-kaggledays
co2_eq_emissions: 68.73074770596023
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 625717986
- CO2 Emissions (in grams): 68.73074770596023

## Validation Metrics

- Loss: 0.859463632106781
- Accuracy: 0.6118427330852181
- Macro F1: 0.6112554383858383
- Micro F1: 0.6118427330852181
- Weighted F1: 0.6112706859556324
- Macro Precision: 0.6121119616189625
- Micro Precision: 0.6118427330852181
- Weighted Precision: 0.6121068719118146
- Macro Recall: 0.6118067898609261
- Micro Recall: 0.6118427330852181
- Weighted Recall: 0.6118427330852181


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Someshfengde/autonlp-kaggledays-625717986
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Someshfengde/autonlp-kaggledays-625717986", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Someshfengde/autonlp-kaggledays-625717986", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```