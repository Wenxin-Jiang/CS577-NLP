---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-17102022_relabel
co2_eq_emissions:
  emissions: 16.970831166674337
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1786061945
- CO2 Emissions (in grams): 16.9708

## Validation Metrics

- Loss: 0.022
- Accuracy: 0.994
- Precision: 0.851
- Recall: 0.885
- F1: 0.868

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-17102022_relabel-1786061945
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-17102022_relabel-1786061945", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-17102022_relabel-1786061945", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```