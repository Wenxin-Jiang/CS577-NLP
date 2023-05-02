---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Awesome7749/autotrain-data-patent-101
co2_eq_emissions:
  emissions: 1.761467513119125
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2952885911
- CO2 Emissions (in grams): 1.7615

## Validation Metrics

- Loss: 0.359
- Accuracy: 0.854
- Precision: 0.744
- Recall: 0.296
- AUC: 0.832
- F1: 0.424

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Awesome7749/autotrain-patent-101-2952885911
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Awesome7749/autotrain-patent-101-2952885911", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Awesome7749/autotrain-patent-101-2952885911", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```