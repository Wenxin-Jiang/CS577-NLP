---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- alecmullen/autonlp-data-group-classification
co2_eq_emissions: 0.4362732160754736
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 441411446
- CO2 Emissions (in grams): 0.4362732160754736

## Validation Metrics

- Loss: 0.7598486542701721
- Accuracy: 0.8222222222222222
- Macro F1: 0.2912091747693842
- Micro F1: 0.8222222222222222
- Weighted F1: 0.7707160863181806
- Macro Precision: 0.29631463146314635
- Micro Precision: 0.8222222222222222
- Weighted Precision: 0.7341339689524508
- Macro Recall: 0.30174603174603176
- Micro Recall: 0.8222222222222222
- Weighted Recall: 0.8222222222222222


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/alecmullen/autonlp-group-classification-441411446
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("alecmullen/autonlp-group-classification-441411446", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("alecmullen/autonlp-group-classification-441411446", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```