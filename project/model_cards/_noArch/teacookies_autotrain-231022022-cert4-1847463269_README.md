---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-231022022-cert4
co2_eq_emissions:
  emissions: 17.781243387408683
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1847463269
- CO2 Emissions (in grams): 17.7812

## Validation Metrics

- Loss: 0.004
- Accuracy: 0.999
- Precision: 0.955
- Recall: 0.969
- F1: 0.962

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-231022022-cert4-1847463269
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-231022022-cert4-1847463269", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-231022022-cert4-1847463269", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```