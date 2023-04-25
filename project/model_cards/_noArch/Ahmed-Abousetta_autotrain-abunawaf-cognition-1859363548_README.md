---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Ahmed-Abousetta/autotrain-data-abunawaf-cognition
co2_eq_emissions:
  emissions: 0.9315924025671088
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1859363548
- CO2 Emissions (in grams): 0.9316

## Validation Metrics

- Loss: 0.392
- Accuracy: 0.837
- Precision: 0.787
- Recall: 0.833
- AUC: 0.900
- F1: 0.810

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-cognition-1859363548
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-1859363548", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-cognition-1859363548", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```