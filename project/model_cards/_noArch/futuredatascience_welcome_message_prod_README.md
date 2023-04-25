---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- lucieackley/autotrain-data-welcome-msg
co2_eq_emissions:
  emissions: 0.004232771974269245
---

# Model Trained On Welcome Messages labeled by Catie

- Problem type: Binary Classification
- Model ID: 2125168670
- CO2 Emissions (in grams): 0.0042

## Validation Metrics

- Loss: 0.244
- Accuracy: 0.958
- Precision: 0.938
- Recall: 1.000
- AUC: 0.970
- F1: 0.968

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/lucieackley/autotrain-welcome-msg-2125168670
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("lucieackley/autotrain-welcome-msg-2125168670", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("lucieackley/autotrain-welcome-msg-2125168670", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```