---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-18112022-cert
co2_eq_emissions:
  emissions: 17.745493294511153
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2140369076
- CO2 Emissions (in grams): 17.7455

## Validation Metrics

- Loss: 0.003
- Accuracy: 0.999
- Precision: 0.986
- Recall: 0.989
- F1: 0.987

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-18112022-cert-2140369076
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-18112022-cert-2140369076", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-18112022-cert-2140369076", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```