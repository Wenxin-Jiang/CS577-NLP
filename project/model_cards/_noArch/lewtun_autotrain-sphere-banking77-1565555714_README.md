---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- lewtun/autotrain-data-sphere-banking77
co2_eq_emissions:
  emissions: 0.040322592546588654
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1565555714
- CO2 Emissions (in grams): 0.0403

## Validation Metrics

- Loss: 0.317
- Accuracy: 0.919
- Macro F1: 0.920
- Micro F1: 0.919
- Weighted F1: 0.920
- Macro Precision: 0.925
- Micro Precision: 0.919
- Weighted Precision: 0.923
- Macro Recall: 0.919
- Micro Recall: 0.919
- Weighted Recall: 0.919


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/lewtun/autotrain-sphere-banking77-1565555714
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("lewtun/autotrain-sphere-banking77-1565555714", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("lewtun/autotrain-sphere-banking77-1565555714", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```