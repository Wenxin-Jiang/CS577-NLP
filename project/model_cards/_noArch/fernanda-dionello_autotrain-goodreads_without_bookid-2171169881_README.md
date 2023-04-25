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
  emissions: 10.018792119596627
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2171169881
- CO2 Emissions (in grams): 10.0188

## Validation Metrics

- Loss: 0.754
- Accuracy: 0.660
- Macro F1: 0.422
- Micro F1: 0.660
- Weighted F1: 0.637
- Macro Precision: 0.418
- Micro Precision: 0.660
- Weighted Precision: 0.631
- Macro Recall: 0.440
- Micro Recall: 0.660
- Weighted Recall: 0.660


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/fernanda-dionello/autotrain-goodreads_without_bookid-2171169881
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("fernanda-dionello/autotrain-goodreads_without_bookid-2171169881", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("fernanda-dionello/autotrain-goodreads_without_bookid-2171169881", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```