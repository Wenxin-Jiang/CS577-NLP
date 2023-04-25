---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-15112022-cert2
co2_eq_emissions:
  emissions: 30.88105111466208
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2099767621
- CO2 Emissions (in grams): 30.8811

## Validation Metrics

- Loss: 0.004
- Accuracy: 0.999
- Precision: 0.982
- Recall: 0.990
- F1: 0.986

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-15112022-cert2-2099767621
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-15112022-cert2-2099767621", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-15112022-cert2-2099767621", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```