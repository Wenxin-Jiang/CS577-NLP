---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-24102022-cert9
co2_eq_emissions:
  emissions: 18.678658475473995
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1861563662
- CO2 Emissions (in grams): 18.6787

## Validation Metrics

- Loss: 0.004
- Accuracy: 0.999
- Precision: 0.959
- Recall: 0.969
- F1: 0.964

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-24102022-cert9-1861563662
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-24102022-cert9-1861563662", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-24102022-cert9-1861563662", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```