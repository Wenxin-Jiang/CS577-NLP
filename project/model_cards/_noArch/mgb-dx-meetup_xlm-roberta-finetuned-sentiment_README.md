---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- lewtun/autotrain-data-mgb-product-reviews-xlm-r
co2_eq_emissions:
  emissions: 19.116414139555882
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1904264758
- CO2 Emissions (in grams): 19.1164

## Validation Metrics

- Loss: 1.021
- Accuracy: 0.563
- Macro F1: 0.555
- Micro F1: 0.563
- Weighted F1: 0.556
- Macro Precision: 0.555
- Micro Precision: 0.563
- Weighted Precision: 0.556
- Macro Recall: 0.562
- Micro Recall: 0.563
- Weighted Recall: 0.563


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/lewtun/autotrain-mgb-product-reviews-xlm-r-1904264758
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("lewtun/autotrain-mgb-product-reviews-xlm-r-1904264758", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("lewtun/autotrain-mgb-product-reviews-xlm-r-1904264758", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```