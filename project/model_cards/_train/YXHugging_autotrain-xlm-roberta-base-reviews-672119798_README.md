---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- YXHugging/autotrain-data-xlm-roberta-base-reviews
co2_eq_emissions: 1013.8825767332373
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 672119798
- CO2 Emissions (in grams): 1013.8825767332373

## Validation Metrics

- Loss: 0.9646632075309753
- Accuracy: 0.5789333333333333
- Macro F1: 0.5775792001871465
- Micro F1: 0.5789333333333333
- Weighted F1: 0.5775792001871465
- Macro Precision: 0.5829444191847423
- Micro Precision: 0.5789333333333333
- Weighted Precision: 0.5829444191847424
- Macro Recall: 0.5789333333333333
- Micro Recall: 0.5789333333333333
- Weighted Recall: 0.5789333333333333


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/YXHugging/autotrain-xlm-roberta-base-reviews-672119798
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("YXHugging/autotrain-xlm-roberta-base-reviews-672119798", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("YXHugging/autotrain-xlm-roberta-base-reviews-672119798", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```