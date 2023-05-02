---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- EricPeter/autotrain-data-comments
co2_eq_emissions:
  emissions: 0.006703744801047603
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1344451577
- CO2 Emissions (in grams): 0.0067

## Validation Metrics

- Loss: 1.080
- Accuracy: 0.619
- Macro F1: 0.360
- Micro F1: 0.619
- Weighted F1: 0.564
- Macro Precision: 0.476
- Micro Precision: 0.619
- Weighted Precision: 0.590
- Macro Recall: 0.344
- Micro Recall: 0.619
- Weighted Recall: 0.619


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/EricPeter/autotrain-comments-1344451577
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("EricPeter/autotrain-comments-1344451577", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("EricPeter/autotrain-comments-1344451577", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```