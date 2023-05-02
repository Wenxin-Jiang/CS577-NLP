---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- PhucLe/autotrain-data-LRO_v1.0.2b
co2_eq_emissions:
  emissions: 5.027600666336915
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1350751935
- CO2 Emissions (in grams): 5.0276

## Validation Metrics

- Loss: 0.685
- Accuracy: 0.833
- Macro F1: 0.833
- Micro F1: 0.833
- Weighted F1: 0.833
- Macro Precision: 0.838
- Micro Precision: 0.833
- Weighted Precision: 0.838
- Macro Recall: 0.833
- Micro Recall: 0.833
- Weighted Recall: 0.833


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/PhucLe/autotrain-LRO_v1.0.2b-1350751935
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("PhucLe/autotrain-LRO_v1.0.2b-1350751935", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("PhucLe/autotrain-LRO_v1.0.2b-1350751935", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```