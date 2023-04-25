---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- LiveEvil/autotrain-data-copuml-production
co2_eq_emissions:
  emissions: 0.9758714074673083
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2205570752
- CO2 Emissions (in grams): 0.9759

## Validation Metrics

- Loss: 1.092
- Accuracy: 0.701
- Macro F1: 0.416
- Micro F1: 0.701
- Weighted F1: 0.670
- Macro Precision: 0.399
- Micro Precision: 0.701
- Weighted Precision: 0.643
- Macro Recall: 0.436
- Micro Recall: 0.701
- Weighted Recall: 0.701


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/LiveEvil/autotrain-copuml-production-2205570752
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("LiveEvil/autotrain-copuml-production-2205570752", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("LiveEvil/autotrain-copuml-production-2205570752", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```