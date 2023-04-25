---
tags:
- autotrain
- text-classification
language:
- fr
widget:
- text: "I love AutoTrain 🤗"
datasets:
- acrowth/autotrain-data-preesmetextclassifier
co2_eq_emissions:
  emissions: 3.3212303373617473
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2437575785
- CO2 Emissions (in grams): 3.3212

## Validation Metrics

- Loss: 0.142
- Accuracy: 0.970
- Macro F1: 0.572
- Micro F1: 0.970
- Weighted F1: 0.960
- Macro Precision: 0.592
- Micro Precision: 0.970
- Weighted Precision: 0.951
- Macro Recall: 0.556
- Micro Recall: 0.970
- Weighted Recall: 0.970


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/acrowth/autotrain-preesmetextclassifier-2437575785
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("acrowth/autotrain-preesmetextclassifier-2437575785", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("acrowth/autotrain-preesmetextclassifier-2437575785", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```