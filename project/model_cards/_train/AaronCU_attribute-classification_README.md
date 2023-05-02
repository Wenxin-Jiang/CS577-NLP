---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- AaronCU/autotrain-data-attribute-classification
co2_eq_emissions:
  emissions: 0.002847008943614719
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1343651539
- CO2 Emissions (in grams): 0.0028

## Validation Metrics

- Loss: 0.163
- Accuracy: 0.949
- Macro F1: 0.947
- Micro F1: 0.949
- Weighted F1: 0.949
- Macro Precision: 0.943
- Micro Precision: 0.949
- Weighted Precision: 0.951
- Macro Recall: 0.952
- Micro Recall: 0.949
- Weighted Recall: 0.949


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/AaronCU/autotrain-attribute-classification-1343651539
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("AaronCU/autotrain-attribute-classification-1343651539", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("AaronCU/autotrain-attribute-classification-1343651539", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```