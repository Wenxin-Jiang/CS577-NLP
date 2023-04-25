---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- pittawat/autotrain-data-twitter-covid-19-spam-detection
co2_eq_emissions:
  emissions: 1.0218403202204225
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2512177276
- CO2 Emissions (in grams): 1.0218

## Validation Metrics

- Loss: 0.275
- Accuracy: 0.906
- Precision: 0.930
- Recall: 0.960
- AUC: 0.882
- F1: 0.945

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/pittawat/autotrain-twitter-covid-19-spam-detection-2512177276
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("pittawat/autotrain-twitter-covid-19-spam-detection-2512177276", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("pittawat/autotrain-twitter-covid-19-spam-detection-2512177276", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```