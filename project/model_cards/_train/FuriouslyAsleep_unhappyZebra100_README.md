---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- FuriouslyAsleep/autotrain-data-techDataClassifeier
co2_eq_emissions: 0.6969569001670619
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 664919631
- CO2 Emissions (in grams): 0.6969569001670619

## Validation Metrics

- Loss: 0.022509008646011353
- Accuracy: 1.0
- Precision: 1.0
- Recall: 1.0
- AUC: 1.0
- F1: 1.0

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/FuriouslyAsleep/autotrain-techDataClassifeier-664919631
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("FuriouslyAsleep/autotrain-techDataClassifeier-664919631", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("FuriouslyAsleep/autotrain-techDataClassifeier-664919631", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```