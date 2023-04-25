---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-21102022-cert
co2_eq_emissions:
  emissions: 19.94429730071814
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1827562840
- CO2 Emissions (in grams): 19.9443

## Validation Metrics

- Loss: 0.028
- Accuracy: 0.992
- Precision: 0.820
- Recall: 0.885
- F1: 0.851

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-21102022-cert-1827562840
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-21102022-cert-1827562840", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-21102022-cert-1827562840", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```