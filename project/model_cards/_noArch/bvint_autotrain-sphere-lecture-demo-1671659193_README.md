---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- bvint/autotrain-data-sphere-lecture-demo
co2_eq_emissions:
  emissions: 0.004735324111068996
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1671659193
- CO2 Emissions (in grams): 0.0047

## Validation Metrics

- Loss: 0.803
- Accuracy: 0.658
- Macro F1: 0.478
- Micro F1: 0.658
- Weighted F1: 0.580
- Macro Precision: 0.424
- Micro Precision: 0.658
- Weighted Precision: 0.520
- Macro Recall: 0.549
- Micro Recall: 0.658
- Weighted Recall: 0.658


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/bvint/autotrain-sphere-lecture-demo-1671659193
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("bvint/autotrain-sphere-lecture-demo-1671659193", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("bvint/autotrain-sphere-lecture-demo-1671659193", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```