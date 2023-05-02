---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- 404E/autotrain-data-formality
co2_eq_emissions: 7.300283563922049
---

# Model Trained Using AutoTrain

- Problem type: Single Column Regression
- Model ID: 1026434913
- CO2 Emissions (in grams): 7.300283563922049

## Validation Metrics

- Loss: 0.5467672348022461
- MSE: 0.5467672944068909
- MAE: 0.5851736068725586
- R2: 0.6883510493648173
- RMSE: 0.7394371628761292
- Explained Variance: 0.6885714530944824

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/404E/autotrain-formality-1026434913
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("404E/autotrain-formality-1026434913", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("404E/autotrain-formality-1026434913", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```