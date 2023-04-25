---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-17102022-cert
co2_eq_emissions:
  emissions: 16.43804270120875
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1781461794
- CO2 Emissions (in grams): 16.4380

## Validation Metrics

- Loss: 0.023
- Accuracy: 0.994
- Precision: 0.821
- Recall: 0.876
- F1: 0.847

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-17102022-cert-1781461794
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-17102022-cert-1781461794", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-17102022-cert-1781461794", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```