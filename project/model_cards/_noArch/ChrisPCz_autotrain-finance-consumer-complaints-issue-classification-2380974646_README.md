---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- ChrisPCz/autotrain-data-finance-consumer-complaints-issue-classification
co2_eq_emissions:
  emissions: 89.45199951708611
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2380974646
- CO2 Emissions (in grams): 89.4520

## Validation Metrics

- Loss: 0.606
- Accuracy: 0.782
- Macro F1: 0.780
- Micro F1: 0.782
- Weighted F1: 0.780
- Macro Precision: 0.780
- Micro Precision: 0.782
- Weighted Precision: 0.780
- Macro Recall: 0.782
- Micro Recall: 0.782
- Weighted Recall: 0.782


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/ChrisPCz/autotrain-finance-consumer-complaints-issue-classification-2380974646
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("ChrisPCz/autotrain-finance-consumer-complaints-issue-classification-2380974646", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("ChrisPCz/autotrain-finance-consumer-complaints-issue-classification-2380974646", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```