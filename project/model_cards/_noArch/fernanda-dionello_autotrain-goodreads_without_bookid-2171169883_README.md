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
  emissions: 7.7592453257413565
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2171169883
- CO2 Emissions (in grams): 7.7592

## Validation Metrics

- Loss: 1.024
- Accuracy: 0.579
- Macro F1: 0.360
- Micro F1: 0.579
- Weighted F1: 0.560
- Macro Precision: 0.383
- Micro Precision: 0.579
- Weighted Precision: 0.553
- Macro Recall: 0.353
- Micro Recall: 0.579
- Weighted Recall: 0.579


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/fernanda-dionello/autotrain-goodreads_without_bookid-2171169883
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("fernanda-dionello/autotrain-goodreads_without_bookid-2171169883", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("fernanda-dionello/autotrain-goodreads_without_bookid-2171169883", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```