---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- fernanda-dionello/autotrain-data-goodreads_without_bookid
co2_eq_emissions:
  emissions: 11.598027053629247
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2171169880
- CO2 Emissions (in grams): 11.5980

## Validation Metrics

- Loss: 0.792
- Accuracy: 0.654
- Macro F1: 0.547
- Micro F1: 0.654
- Weighted F1: 0.649
- Macro Precision: 0.594
- Micro Precision: 0.654
- Weighted Precision: 0.660
- Macro Recall: 0.530
- Micro Recall: 0.654
- Weighted Recall: 0.654


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/fernanda-dionello/autotrain-goodreads_without_bookid-2171169880
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("fernanda-dionello/autotrain-goodreads_without_bookid-2171169880", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("fernanda-dionello/autotrain-goodreads_without_bookid-2171169880", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```