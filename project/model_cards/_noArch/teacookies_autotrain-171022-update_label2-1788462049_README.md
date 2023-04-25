---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-171022-update_label2
co2_eq_emissions:
  emissions: 19.661735872263936
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1788462049
- CO2 Emissions (in grams): 19.6617

## Validation Metrics

- Loss: 0.031
- Accuracy: 0.991
- Precision: 0.755
- Recall: 0.812
- F1: 0.783

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-171022-update_label2-1788462049
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-171022-update_label2-1788462049", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-171022-update_label2-1788462049", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```