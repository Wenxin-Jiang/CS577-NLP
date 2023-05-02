---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- agnihotri/autotrain-data-contract_type
co2_eq_emissions: 0.07610944071640048
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 809725368
- CO2 Emissions (in grams): 0.07610944071640048

## Validation Metrics

- Loss: 0.05312908813357353
- Accuracy: 0.9911504424778761
- Macro F1: 0.9912087912087912
- Micro F1: 0.9911504424778761
- Weighted F1: 0.9908586988233007
- Macro Precision: 0.9942857142857143
- Micro Precision: 0.9911504424778761
- Weighted Precision: 0.9924146649810366
- Macro Recall: 0.99
- Micro Recall: 0.9911504424778761
- Weighted Recall: 0.9911504424778761


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/agnihotri/autotrain-contract_type-809725368
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("agnihotri/autotrain-contract_type-809725368", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("agnihotri/autotrain-contract_type-809725368", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```