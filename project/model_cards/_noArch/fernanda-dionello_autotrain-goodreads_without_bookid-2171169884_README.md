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
  emissions: 21.014243837592847
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2171169884
- CO2 Emissions (in grams): 21.0142

## Validation Metrics

- Loss: 0.815
- Accuracy: 0.666
- Macro F1: 0.454
- Micro F1: 0.666
- Weighted F1: 0.649
- Macro Precision: 0.465
- Micro Precision: 0.666
- Weighted Precision: 0.638
- Macro Recall: 0.454
- Micro Recall: 0.666
- Weighted Recall: 0.666


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/fernanda-dionello/autotrain-goodreads_without_bookid-2171169884
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("fernanda-dionello/autotrain-goodreads_without_bookid-2171169884", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("fernanda-dionello/autotrain-goodreads_without_bookid-2171169884", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```