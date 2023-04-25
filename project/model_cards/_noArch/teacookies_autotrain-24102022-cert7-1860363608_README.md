---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-24102022-cert7
co2_eq_emissions:
  emissions: 0.0825722192587215
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1860363608
- CO2 Emissions (in grams): 0.0826

## Validation Metrics

- Loss: 0.002
- Accuracy: 0.999
- Precision: 0.972
- Recall: 0.983
- F1: 0.978

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-24102022-cert7-1860363608
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-24102022-cert7-1860363608", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-24102022-cert7-1860363608", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```