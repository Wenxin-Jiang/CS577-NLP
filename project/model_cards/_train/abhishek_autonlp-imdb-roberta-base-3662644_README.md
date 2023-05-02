---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- abhishek/autonlp-data-imdb-roberta-base
co2_eq_emissions: 25.894117734124272
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 3662644
- CO2 Emissions (in grams): 25.894117734124272

## Validation Metrics

- Loss: 0.20277436077594757
- Accuracy: 0.92604
- Precision: 0.9560674830864092
- Recall: 0.89312
- AUC: 0.9814625504000001
- F1: 0.9235223559581421

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-imdb-roberta-base-3662644
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-imdb-roberta-base-3662644", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-imdb-roberta-base-3662644", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```