---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Awesome7749/autotrain-data-patent-101
co2_eq_emissions:
  emissions: 3.7522636525320645
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2952885909
- CO2 Emissions (in grams): 3.7523

## Validation Metrics

- Loss: 0.353
- Accuracy: 0.851
- Precision: 0.598
- Recall: 0.537
- AUC: 0.846
- F1: 0.566

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Awesome7749/autotrain-patent-101-2952885909
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Awesome7749/autotrain-patent-101-2952885909", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Awesome7749/autotrain-patent-101-2952885909", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```