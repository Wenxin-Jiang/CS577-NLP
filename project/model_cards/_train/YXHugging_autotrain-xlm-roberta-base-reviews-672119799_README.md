---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- YXHugging/autotrain-data-xlm-roberta-base-reviews
co2_eq_emissions: 1583.7188188958198
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 672119799
- CO2 Emissions (in grams): 1583.7188188958198

## Validation Metrics

- Loss: 0.9590993523597717
- Accuracy: 0.5827541666666667
- Macro F1: 0.5806748283026683
- Micro F1: 0.5827541666666667
- Weighted F1: 0.5806748283026683
- Macro Precision: 0.5834325027348383
- Micro Precision: 0.5827541666666667
- Weighted Precision: 0.5834325027348383
- Macro Recall: 0.5827541666666667
- Micro Recall: 0.5827541666666667
- Weighted Recall: 0.5827541666666667


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/YXHugging/autotrain-xlm-roberta-base-reviews-672119799
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("YXHugging/autotrain-xlm-roberta-base-reviews-672119799", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("YXHugging/autotrain-xlm-roberta-base-reviews-672119799", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```