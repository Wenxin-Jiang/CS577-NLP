---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-16112022-cert
co2_eq_emissions:
  emissions: 0.08699410121541305
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2114268313
- CO2 Emissions (in grams): 0.0870

## Validation Metrics

- Loss: 0.003
- Accuracy: 0.999
- Precision: 0.987
- Recall: 0.986
- F1: 0.986

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-16112022-cert-2114268313
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-16112022-cert-2114268313", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-16112022-cert-2114268313", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```