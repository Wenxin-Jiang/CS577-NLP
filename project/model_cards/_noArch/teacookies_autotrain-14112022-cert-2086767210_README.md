---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-14112022-cert
co2_eq_emissions:
  emissions: 18.953935307959163
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2086767210
- CO2 Emissions (in grams): 18.9539

## Validation Metrics

- Loss: 0.002
- Accuracy: 1.000
- Precision: 0.987
- Recall: 0.989
- F1: 0.988

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-14112022-cert-2086767210
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-14112022-cert-2086767210", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-14112022-cert-2086767210", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```