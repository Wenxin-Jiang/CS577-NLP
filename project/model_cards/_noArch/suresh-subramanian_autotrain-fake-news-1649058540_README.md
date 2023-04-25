---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- suresh-subramanian/autotrain-data-fake-news
co2_eq_emissions:
  emissions: 4.630852478388675
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1649058540
- CO2 Emissions (in grams): 4.6309

## Validation Metrics

- Loss: 0.527
- Accuracy: 0.725
- Precision: 0.729
- Recall: 0.408
- AUC: 0.825
- F1: 0.523

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/suresh-subramanian/autotrain-fake-news-1649058540
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("suresh-subramanian/autotrain-fake-news-1649058540", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("suresh-subramanian/autotrain-fake-news-1649058540", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```