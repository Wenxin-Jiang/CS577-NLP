---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- NicholasSynovic/autotrain-data-test
co2_eq_emissions:
  emissions: 0.6063524119726759
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2306572976
- CO2 Emissions (in grams): 0.6064

## Validation Metrics

- Loss: 0.345
- Accuracy: 0.876
- Precision: 0.909
- Recall: 0.920
- AUC: 0.924
- F1: 0.914

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/NicholasSynovic/autotrain-test-2306572976
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("NicholasSynovic/autotrain-test-2306572976", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("NicholasSynovic/autotrain-test-2306572976", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```