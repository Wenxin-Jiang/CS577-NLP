---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Crasher222/autonlp-data-kaggle-test
co2_eq_emissions: 60.744727079482495
---

# Model Finetuned from BERT-base for

- Problem type: Multi-class Classification
- Model ID: 25805800

## Validation Metrics

- Loss: 0.4422711133956909
- Accuracy: 0.8615328555811976
- Macro F1: 0.8642434650461513
- Micro F1: 0.8615328555811976
- Weighted F1: 0.8617743626671308
- Macro Precision: 0.8649112225076049
- Micro Precision: 0.8615328555811976
- Weighted Precision: 0.8625407179375096
- Macro Recall: 0.8640777539828228
- Micro Recall: 0.8615328555811976
- Weighted Recall: 0.8615328555811976


## Usage

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Crasher222/kaggle-comp-test")

tokenizer = AutoTokenizer.from_pretrained("Crasher222/kaggle-comp-test")

inputs = tokenizer("I am in love with you", return_tensors="pt")

outputs = model(**inputs)
```