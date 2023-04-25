---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- pachi107/autotrain-data-ethos-sentiments
co2_eq_emissions:
  emissions: 2.331522912581982
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1790262083
- CO2 Emissions (in grams): 2.3315

## Validation Metrics

- Loss: 0.578
- Accuracy: 0.720
- Precision: 0.705
- Recall: 0.867
- AUC: 0.769
- F1: 0.778

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/pachi107/autotrain-ethos-sentiments-1790262083
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("pachi107/autotrain-ethos-sentiments-1790262083", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("pachi107/autotrain-ethos-sentiments-1790262083", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```