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
  emissions: 1.1703390276575862
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1790262080
- CO2 Emissions (in grams): 1.1703

## Validation Metrics

- Loss: 0.469
- Accuracy: 0.830
- Precision: 0.856
- Recall: 0.841
- AUC: 0.898
- F1: 0.848

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/pachi107/autotrain-ethos-sentiments-1790262080
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("pachi107/autotrain-ethos-sentiments-1790262080", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("pachi107/autotrain-ethos-sentiments-1790262080", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```