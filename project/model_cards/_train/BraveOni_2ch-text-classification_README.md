---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- BraveOni/autotrain-data-2ch-text-classification
co2_eq_emissions: 0.08564281067919652
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 955631800
- CO2 Emissions (in grams): 0.08564281067919652

## Validation Metrics

- Loss: 0.34108611941337585
- Accuracy: 0.8671983356449375
- Precision: 0.7883283877349159
- Recall: 0.8250517598343685
- AUC: 0.9236450689447471
- F1: 0.8062721294891249

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/BraveOni/autotrain-2ch-text-classification-955631800
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("BraveOni/autotrain-2ch-text-classification-955631800", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("BraveOni/autotrain-2ch-text-classification-955631800", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```