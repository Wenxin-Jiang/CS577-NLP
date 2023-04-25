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
  emissions: 0.8181506582658064
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1790262082
- CO2 Emissions (in grams): 0.8182

## Validation Metrics

- Loss: 0.565
- Accuracy: 0.775
- Precision: 0.783
- Recall: 0.832
- AUC: 0.823
- F1: 0.807

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/pachi107/autotrain-ethos-sentiments-1790262082
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("pachi107/autotrain-ethos-sentiments-1790262082", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("pachi107/autotrain-ethos-sentiments-1790262082", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```