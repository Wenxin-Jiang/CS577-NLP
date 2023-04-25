---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- JamesH/autotrain-data-third-project
co2_eq_emissions:
  emissions: 6.9919208994196795
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1883864250
- CO2 Emissions (in grams): 6.9919

## Validation Metrics

- Loss: 0.175
- Accuracy: 0.950
- Precision: 0.950
- Recall: 0.950
- AUC: 0.986
- F1: 0.950

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/JamesH/autotrain-third-project-1883864250
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("JamesH/autotrain-third-project-1883864250", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("JamesH/autotrain-third-project-1883864250", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```