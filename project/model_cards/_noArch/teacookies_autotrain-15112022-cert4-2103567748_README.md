---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-15112022-cert4
co2_eq_emissions:
  emissions: 18.550679640609356
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2103567748
- CO2 Emissions (in grams): 18.5507

## Validation Metrics

- Loss: 0.002
- Accuracy: 1.000
- Precision: 0.990
- Recall: 0.992
- F1: 0.991

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-15112022-cert4-2103567748
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-15112022-cert4-2103567748", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-15112022-cert4-2103567748", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```