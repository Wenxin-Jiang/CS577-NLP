---
tags: autonlp
language: ar
widget:
- text: "I love AutoNLP 🤗"
datasets:
- adelgasmi/autonlp-data-kpmg_nlp
co2_eq_emissions: 64.58945483765274
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 18833547
- CO2 Emissions (in grams): 64.58945483765274

## Validation Metrics

- Loss: 0.14247722923755646
- Accuracy: 0.9586074193404036
- Macro F1: 0.9468339778730883
- Micro F1: 0.9586074193404036
- Weighted F1: 0.9585551117678807
- Macro Precision: 0.9445436604001405
- Micro Precision: 0.9586074193404036
- Weighted Precision: 0.9591405429662925
- Macro Recall: 0.9499427161888565
- Micro Recall: 0.9586074193404036
- Weighted Recall: 0.9586074193404036


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/adelgasmi/autonlp-kpmg_nlp-18833547
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("adelgasmi/autonlp-kpmg_nlp-18833547", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("adelgasmi/autonlp-kpmg_nlp-18833547", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```