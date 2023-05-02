---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- YXHugging/autotrain-data-xlm-roberta-base-reviews
co2_eq_emissions: 1019.0229633198007
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 672119797
- CO2 Emissions (in grams): 1019.0229633198007

## Validation Metrics

- Loss: 0.9898674488067627
- Accuracy: 0.5688083333333334
- Macro F1: 0.5640966271895913
- Micro F1: 0.5688083333333334
- Weighted F1: 0.5640966271895913
- Macro Precision: 0.5673737438011194
- Micro Precision: 0.5688083333333334
- Weighted Precision: 0.5673737438011194
- Macro Recall: 0.5688083333333334
- Micro Recall: 0.5688083333333334
- Weighted Recall: 0.5688083333333334


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/YXHugging/autotrain-xlm-roberta-base-reviews-672119797
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("YXHugging/autotrain-xlm-roberta-base-reviews-672119797", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("YXHugging/autotrain-xlm-roberta-base-reviews-672119797", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```