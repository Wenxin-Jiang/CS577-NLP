---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- poldham/autotrain-data-textcat-paul
co2_eq_emissions:
  emissions: 7.014613433979796
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2315373253
- CO2 Emissions (in grams): 7.0146

## Validation Metrics

- Loss: 0.183
- Accuracy: 0.944
- Precision: 0.953
- Recall: 0.931
- AUC: 0.974
- F1: 0.942

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/poldham/autotrain-textcat-paul-2315373253
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("poldham/autotrain-textcat-paul-2315373253", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("poldham/autotrain-textcat-paul-2315373253", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```