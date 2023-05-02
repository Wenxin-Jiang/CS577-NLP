---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- YXHugging/autotrain-data-xlm-roberta-base-reviews
co2_eq_emissions: 2011.6528745969179
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 672119800
- CO2 Emissions (in grams): 2011.6528745969179

## Validation Metrics

- Loss: 0.9570887088775635
- Accuracy: 0.5830708333333333
- Macro F1: 0.5789149828346194
- Micro F1: 0.5830708333333333
- Weighted F1: 0.5789149828346193
- Macro Precision: 0.5808338093704437
- Micro Precision: 0.5830708333333333
- Weighted Precision: 0.5808338093704437
- Macro Recall: 0.5830708333333334
- Micro Recall: 0.5830708333333333
- Weighted Recall: 0.5830708333333333


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/YXHugging/autotrain-xlm-roberta-base-reviews-672119800
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("YXHugging/autotrain-xlm-roberta-base-reviews-672119800", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("YXHugging/autotrain-xlm-roberta-base-reviews-672119800", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```