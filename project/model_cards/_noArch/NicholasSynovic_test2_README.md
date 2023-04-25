---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- NicholasSynovic/autotrain-data-test2
co2_eq_emissions:
  emissions: 0.9679834304164027
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2308373008
- CO2 Emissions (in grams): 0.9680

## Validation Metrics

- Loss: 0.415
- Accuracy: 0.812
- Precision: 0.851
- Recall: 0.895
- AUC: 0.861
- F1: 0.872

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/NicholasSynovic/autotrain-test2-2308373008
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("NicholasSynovic/autotrain-test2-2308373008", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("NicholasSynovic/autotrain-test2-2308373008", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```