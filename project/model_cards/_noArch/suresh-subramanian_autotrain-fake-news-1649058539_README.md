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
  emissions: 0.040297872306469855
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1649058539
- CO2 Emissions (in grams): 0.0403

## Validation Metrics

- Loss: 0.478
- Accuracy: 0.779
- Precision: 0.814
- Recall: 0.520
- AUC: 0.881
- F1: 0.635

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/suresh-subramanian/autotrain-fake-news-1649058539
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("suresh-subramanian/autotrain-fake-news-1649058539", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("suresh-subramanian/autotrain-fake-news-1649058539", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```