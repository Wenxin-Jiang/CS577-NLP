---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- kem000123/autotrain-data-model2-text-class
co2_eq_emissions:
  emissions: 3.652284357860415
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1843563203
- CO2 Emissions (in grams): 3.6523

## Validation Metrics

- Loss: 0.202
- Accuracy: 0.921
- Precision: 0.803
- Recall: 0.862
- AUC: 0.966
- F1: 0.832

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/kem000123/autotrain-model2-text-class-1843563203
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("kem000123/autotrain-model2-text-class-1843563203", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("kem000123/autotrain-model2-text-class-1843563203", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```