---
tags:
- autotrain
- text-classification
language:
- zh
widget:
- text: "I love AutoTrain 🤗"
datasets:
- paulkm/autotrain-data-lottery_v2
co2_eq_emissions:
  emissions: 0.013953144730323944
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2420075390
- CO2 Emissions (in grams): 0.0140

## Validation Metrics

- Loss: 0.117
- Accuracy: 0.966
- Precision: 0.965
- Recall: 0.960
- AUC: 0.990
- F1: 0.962

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/paulkm/autotrain-lottery_v2-2420075390
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("paulkm/autotrain-lottery_v2-2420075390", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("paulkm/autotrain-lottery_v2-2420075390", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```