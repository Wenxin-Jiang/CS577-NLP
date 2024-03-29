---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- YXHugging/autotrain-data-xlm-roberta-base-reviews
co2_eq_emissions: 999.5670927087938
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 672119801
- CO2 Emissions (in grams): 999.5670927087938

## Validation Metrics

- Loss: 0.9767692685127258
- Accuracy: 0.5738333333333333
- Macro F1: 0.5698748846905103
- Micro F1: 0.5738333333333333
- Weighted F1: 0.5698748846905102
- Macro Precision: 0.5734242161804903
- Micro Precision: 0.5738333333333333
- Weighted Precision: 0.5734242161804902
- Macro Recall: 0.5738333333333333
- Micro Recall: 0.5738333333333333
- Weighted Recall: 0.5738333333333333


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/YXHugging/autotrain-xlm-roberta-base-reviews-672119801
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("YXHugging/autotrain-xlm-roberta-base-reviews-672119801", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("YXHugging/autotrain-xlm-roberta-base-reviews-672119801", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```