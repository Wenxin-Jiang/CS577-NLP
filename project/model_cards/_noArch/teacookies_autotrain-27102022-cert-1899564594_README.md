---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-27102022-cert
co2_eq_emissions:
  emissions: 22.03607609264655
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1899564594
- CO2 Emissions (in grams): 22.0361

## Validation Metrics

- Loss: 0.003
- Accuracy: 0.999
- Precision: 0.981
- Recall: 0.982
- F1: 0.981

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-27102022-cert-1899564594
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-27102022-cert-1899564594", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-27102022-cert-1899564594", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```