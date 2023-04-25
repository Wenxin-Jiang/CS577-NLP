---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-17102022133-cert
co2_eq_emissions:
  emissions: 20.262915394129607
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1781761805
- CO2 Emissions (in grams): 20.2629

## Validation Metrics

- Loss: 0.017
- Accuracy: 0.995
- Precision: 0.824
- Recall: 0.865
- F1: 0.844

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-17102022133-cert-1781761805
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-17102022133-cert-1781761805", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-17102022133-cert-1781761805", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```