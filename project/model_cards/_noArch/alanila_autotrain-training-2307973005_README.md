---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- alanila/autotrain-data-training
co2_eq_emissions:
  emissions: 3.7679548759427006
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2307973005
- CO2 Emissions (in grams): 3.7680

## Validation Metrics

- Loss: 1.098
- Accuracy: 0.508
- Macro F1: 0.559
- Micro F1: 0.508
- Weighted F1: 0.452
- Macro Precision: 0.610
- Micro Precision: 0.508
- Weighted Precision: 0.537
- Macro Recall: 0.581
- Micro Recall: 0.508
- Weighted Recall: 0.508


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/alanila/autotrain-training-2307973005
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("alanila/autotrain-training-2307973005", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("alanila/autotrain-training-2307973005", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```