---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- lewtun/autotrain-data-mgb-product-reviews-mbert
co2_eq_emissions:
  emissions: 5.523107849339405
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1904564767
- CO2 Emissions (in grams): 5.5231

## Validation Metrics

- Loss: 1.135
- Accuracy: 0.514
- Macro F1: 0.504
- Micro F1: 0.514
- Weighted F1: 0.505
- Macro Precision: 0.506
- Micro Precision: 0.514
- Weighted Precision: 0.507
- Macro Recall: 0.513
- Micro Recall: 0.514
- Weighted Recall: 0.514


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/lewtun/autotrain-mgb-product-reviews-mbert-1904564767
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("lewtun/autotrain-mgb-product-reviews-mbert-1904564767", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("lewtun/autotrain-mgb-product-reviews-mbert-1904564767", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```