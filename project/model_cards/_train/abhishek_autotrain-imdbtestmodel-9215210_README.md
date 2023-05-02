---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- abhishek/autotrain-data-imdbtestmodel
co2_eq_emissions: 0.2757084122251468
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 9215210
- CO2 Emissions (in grams): 0.2757084122251468

## Validation Metrics

- Loss: 0.1699502319097519
- Accuracy: 0.9372
- Precision: 0.9277551659361303
- Recall: 0.94824
- AUC: 0.9837227744
- F1: 0.9378857414147808

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/abhishek/autotrain-imdbtestmodel-9215210
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autotrain-imdbtestmodel-9215210", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autotrain-imdbtestmodel-9215210", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```