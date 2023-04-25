---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-15112022-cert8
co2_eq_emissions:
  emissions: 0.09525840317901095
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2105867883
- CO2 Emissions (in grams): 0.0953

## Validation Metrics

- Loss: 0.003
- Accuracy: 0.999
- Precision: 0.984
- Recall: 0.989
- F1: 0.986

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-15112022-cert8-2105867883
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-15112022-cert8-2105867883", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-15112022-cert8-2105867883", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```