---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-17102022-cert_update_date
co2_eq_emissions:
  emissions: 18.37074974959855
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1786462003
- CO2 Emissions (in grams): 18.3707

## Validation Metrics

- Loss: 0.019
- Accuracy: 0.995
- Precision: 0.835
- Recall: 0.867
- F1: 0.851

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-17102022-cert_update_date-1786462003
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-17102022-cert_update_date-1786462003", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-17102022-cert_update_date-1786462003", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```