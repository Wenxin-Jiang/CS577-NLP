---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-15112022-cert7
co2_eq_emissions:
  emissions: 0.08177433184040792
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2105067828
- CO2 Emissions (in grams): 0.0818

## Validation Metrics

- Loss: 0.002
- Accuracy: 0.999
- Precision: 0.991
- Recall: 0.992
- F1: 0.991

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-15112022-cert7-2105067828
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-15112022-cert7-2105067828", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-15112022-cert7-2105067828", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```