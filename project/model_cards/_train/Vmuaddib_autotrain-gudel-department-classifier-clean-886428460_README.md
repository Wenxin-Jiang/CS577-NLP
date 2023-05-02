---
tags: [autotrain]
language: de
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Vmuaddib/autotrain-data-gudel-department-classifier-clean
co2_eq_emissions: 14.294320632050567
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 886428460
- CO2 Emissions (in grams): 14.294320632050567

## Validation Metrics

- Loss: 0.051413487643003464
- Accuracy: 0.9894490035169988
- Precision: 1.0
- Recall: 0.9862174578866769
- AUC: 0.9989318529862175
- F1: 0.9930609097918273

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Vmuaddib/autotrain-gudel-department-classifier-clean-886428460
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Vmuaddib/autotrain-gudel-department-classifier-clean-886428460", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Vmuaddib/autotrain-gudel-department-classifier-clean-886428460", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```