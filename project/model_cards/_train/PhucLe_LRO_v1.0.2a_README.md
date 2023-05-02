---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- PhucLe/autotrain-data-LRO_v1.0.2
co2_eq_emissions:
  emissions: 1.2585708613878817
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1345851607
- CO2 Emissions (in grams): 1.2586

## Validation Metrics

- Loss: 0.523
- Accuracy: 0.818
- Macro F1: 0.817
- Micro F1: 0.818
- Weighted F1: 0.817
- Macro Precision: 0.824
- Micro Precision: 0.818
- Weighted Precision: 0.824
- Macro Recall: 0.818
- Micro Recall: 0.818
- Weighted Recall: 0.818


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/PhucLe/autotrain-LRO_v1.0.2-1345851607
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("PhucLe/autotrain-LRO_v1.0.2-1345851607", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("PhucLe/autotrain-LRO_v1.0.2-1345851607", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```