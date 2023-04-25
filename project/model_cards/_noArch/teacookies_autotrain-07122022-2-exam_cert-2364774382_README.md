---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-07122022-2-exam_cert
co2_eq_emissions:
  emissions: 24.71153691821318
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2364774382
- CO2 Emissions (in grams): 24.7115

## Validation Metrics

- Loss: 0.021
- Accuracy: 0.995
- Precision: 0.917
- Recall: 0.932
- F1: 0.924

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-07122022-2-exam_cert-2364774382
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-07122022-2-exam_cert-2364774382", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-07122022-2-exam_cert-2364774382", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```