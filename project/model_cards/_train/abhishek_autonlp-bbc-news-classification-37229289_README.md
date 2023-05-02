---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- abhishek/autonlp-data-bbc-news-classification
co2_eq_emissions: 5.448567309047846
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 37229289
- CO2 Emissions (in grams): 5.448567309047846

## Validation Metrics

- Loss: 0.07081354409456253
- Accuracy: 0.9867109634551495
- Macro F1: 0.9859067529980614
- Micro F1: 0.9867109634551495
- Weighted F1: 0.9866417220968429
- Macro Precision: 0.9868771404595043
- Micro Precision: 0.9867109634551495
- Weighted Precision: 0.9869289511551576
- Macro Recall: 0.9853173241852486
- Micro Recall: 0.9867109634551495
- Weighted Recall: 0.9867109634551495


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-bbc-news-classification-37229289
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-bbc-news-classification-37229289", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-bbc-news-classification-37229289", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```