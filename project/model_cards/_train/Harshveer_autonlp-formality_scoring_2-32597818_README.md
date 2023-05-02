---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Harshveer/autonlp-data-formality_scoring_2
co2_eq_emissions: 8.655894631203154
---

# Model Trained Using AutoNLP

- Problem type: Single Column Regression
- Model ID: 32597818
- CO2 Emissions (in grams): 8.655894631203154

## Validation Metrics

- Loss: 0.5410276651382446
- MSE: 0.5410276651382446
- MAE: 0.5694561004638672
- R2: 0.6830431129198475
- RMSE: 0.735545814037323
- Explained Variance: 0.6834385395050049

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Harshveer/autonlp-formality_scoring_2-32597818
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Harshveer/autonlp-formality_scoring_2-32597818", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Harshveer/autonlp-formality_scoring_2-32597818", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```