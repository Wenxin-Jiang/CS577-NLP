---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- BenWord/autotrain-data-APM2
co2_eq_emissions:
  emissions: 2.355843472980154
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1212245840
- CO2 Emissions (in grams): 2.3558

## Validation Metrics

- Loss: 0.018
- Accuracy: 1.000
- Precision: 1.000
- Recall: 1.000
- AUC: 1.000
- F1: 1.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/BenWord/autotrain-APM2-1212245840
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("BenWord/autotrain-APM2-1212245840", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("BenWord/autotrain-APM2-1212245840", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```