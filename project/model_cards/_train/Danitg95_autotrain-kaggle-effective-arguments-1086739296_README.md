---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Danitg95/autotrain-data-kaggle-effective-arguments
co2_eq_emissions: 5.2497206864306065
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1086739296
- CO2 Emissions (in grams): 5.2497206864306065

## Validation Metrics

- Loss: 0.744236171245575
- Accuracy: 0.6719238613188308
- Macro F1: 0.5450301061253738
- Micro F1: 0.6719238613188308
- Weighted F1: 0.6349879540623229
- Macro Precision: 0.6691326843926052
- Micro Precision: 0.6719238613188308
- Weighted Precision: 0.6706209016443158
- Macro Recall: 0.5426627824078865
- Micro Recall: 0.6719238613188308
- Weighted Recall: 0.6719238613188308


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Danitg95/autotrain-kaggle-effective-arguments-1086739296
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Danitg95/autotrain-kaggle-effective-arguments-1086739296", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Danitg95/autotrain-kaggle-effective-arguments-1086739296", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```