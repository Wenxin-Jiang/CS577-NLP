---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-16112022-cert2
co2_eq_emissions:
  emissions: 20.851244285270415
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2115868392
- CO2 Emissions (in grams): 20.8512

## Validation Metrics

- Loss: 0.003
- Accuracy: 0.999
- Precision: 0.984
- Recall: 0.984
- F1: 0.984

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-16112022-cert2-2115868392
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-16112022-cert2-2115868392", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-16112022-cert2-2115868392", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```