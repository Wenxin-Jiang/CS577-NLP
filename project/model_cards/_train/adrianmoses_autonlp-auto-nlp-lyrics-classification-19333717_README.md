---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- adrianmoses/autonlp-data-auto-nlp-lyrics-classification
co2_eq_emissions: 88.89388195672073
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 19333717
- CO2 Emissions (in grams): 88.89388195672073

## Validation Metrics

- Loss: 1.0499154329299927
- Accuracy: 0.6207088513638894
- Macro F1: 0.46250803661544765
- Micro F1: 0.6207088513638894
- Weighted F1: 0.5850362079928957
- Macro Precision: 0.6451479987704787
- Micro Precision: 0.6207088513638894
- Weighted Precision: 0.6285080101186085
- Macro Recall: 0.4405680478429344
- Micro Recall: 0.6207088513638894
- Weighted Recall: 0.6207088513638894


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/adrianmoses/autonlp-auto-nlp-lyrics-classification-19333717
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("adrianmoses/autonlp-auto-nlp-lyrics-classification-19333717", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("adrianmoses/autonlp-auto-nlp-lyrics-classification-19333717", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```