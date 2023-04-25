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
  emissions: 6.409243088343928
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2171169882
- CO2 Emissions (in grams): 6.4092

## Validation Metrics

- Loss: 0.950
- Accuracy: 0.586
- Macro F1: 0.373
- Micro F1: 0.586
- Weighted F1: 0.564
- Macro Precision: 0.438
- Micro Precision: 0.586
- Weighted Precision: 0.575
- Macro Recall: 0.399
- Micro Recall: 0.586
- Weighted Recall: 0.586


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/fernanda-dionello/autotrain-goodreads_without_bookid-2171169882
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("fernanda-dionello/autotrain-goodreads_without_bookid-2171169882", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("fernanda-dionello/autotrain-goodreads_without_bookid-2171169882", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```