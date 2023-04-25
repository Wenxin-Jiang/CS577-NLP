---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- rgoldstein/autotrain-data-movie-rationales
co2_eq_emissions:
  emissions: 5.912842155368309
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1734060527
- CO2 Emissions (in grams): 5.9128

## Validation Metrics

- Loss: 0.198
- Accuracy: 0.934
- Precision: 0.937
- Recall: 0.931
- AUC: 0.983
- F1: 0.934

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/rgoldstein/autotrain-movie-rationales-1734060527
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("rgoldstein/autotrain-movie-rationales-1734060527", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("rgoldstein/autotrain-movie-rationales-1734060527", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```