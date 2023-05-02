---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- aaazzzz/autotrain-data-cuisine_classification
co2_eq_emissions:
  emissions: 181.03886827858415
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1361652530
- CO2 Emissions (in grams): 181.0389

## Validation Metrics

- Loss: 0.920
- Accuracy: 0.731
- Macro F1: 0.669
- Micro F1: 0.731
- Weighted F1: 0.726
- Macro Precision: 0.774
- Micro Precision: 0.731
- Weighted Precision: 0.738
- Macro Recall: 0.623
- Micro Recall: 0.731
- Weighted Recall: 0.731


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/aaazzzz/autotrain-cuisine_classification-1361652530
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("aaazzzz/autotrain-cuisine_classification-1361652530", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("aaazzzz/autotrain-cuisine_classification-1361652530", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```