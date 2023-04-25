---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- alanila/autotrain-data-training
co2_eq_emissions:
  emissions: 1.2620473255629743
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2307973004
- CO2 Emissions (in grams): 1.2620

## Validation Metrics

- Loss: 1.279
- Accuracy: 0.517
- Macro F1: 0.549
- Micro F1: 0.517
- Weighted F1: 0.443
- Macro Precision: 0.585
- Micro Precision: 0.517
- Weighted Precision: 0.480
- Macro Recall: 0.572
- Micro Recall: 0.517
- Weighted Recall: 0.517


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/alanila/autotrain-training-2307973004
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("alanila/auto_train", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("alanila/auto_train", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```