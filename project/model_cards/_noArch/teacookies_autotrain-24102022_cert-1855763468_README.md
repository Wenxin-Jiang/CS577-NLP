---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-24102022_cert
co2_eq_emissions:
  emissions: 15.043841231531312
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1855763468
- CO2 Emissions (in grams): 15.0438

## Validation Metrics

- Loss: 0.005
- Accuracy: 0.999
- Precision: 0.942
- Recall: 0.952
- F1: 0.947

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-24102022_cert-1855763468
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-24102022_cert-1855763468", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-24102022_cert-1855763468", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```