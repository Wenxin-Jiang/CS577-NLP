---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-24102022-cert4
co2_eq_emissions:
  emissions: 19.82493725454133
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1858363508
- CO2 Emissions (in grams): 19.8249

## Validation Metrics

- Loss: 0.003
- Accuracy: 0.999
- Precision: 0.963
- Recall: 0.971
- F1: 0.967

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-24102022-cert4-1858363508
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-24102022-cert4-1858363508", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-24102022-cert4-1858363508", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```