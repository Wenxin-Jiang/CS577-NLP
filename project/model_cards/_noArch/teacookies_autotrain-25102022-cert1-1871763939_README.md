---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-25102022-cert1
co2_eq_emissions:
  emissions: 22.29520077707259
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1871763939
- CO2 Emissions (in grams): 22.2952

## Validation Metrics

- Loss: 0.002
- Accuracy: 0.999
- Precision: 0.972
- Recall: 0.978
- F1: 0.975

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-25102022-cert1-1871763939
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-25102022-cert1-1871763939", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-25102022-cert1-1871763939", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```