---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-27102022-cert1
co2_eq_emissions:
  emissions: 16.254745105263574
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1899464570
- CO2 Emissions (in grams): 16.2547

## Validation Metrics

- Loss: 0.004
- Accuracy: 0.999
- Precision: 0.972
- Recall: 0.979
- F1: 0.975

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-27102022-cert1-1899464570
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-27102022-cert1-1899464570", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-27102022-cert1-1899464570", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```