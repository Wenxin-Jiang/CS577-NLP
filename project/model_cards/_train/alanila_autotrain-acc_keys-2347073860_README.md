---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- alanila/autotrain-data-acc_keys
co2_eq_emissions:
  emissions: 1.3599341780747405
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2347073860
- CO2 Emissions (in grams): 1.3599

## Validation Metrics

- Loss: 1.255
- Accuracy: 0.500
- Macro F1: 0.445
- Micro F1: 0.500
- Weighted F1: 0.421
- Macro Precision: 0.498
- Micro Precision: 0.500
- Weighted Precision: 0.508
- Macro Recall: 0.481
- Micro Recall: 0.500
- Weighted Recall: 0.500


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/alanila/autotrain-acc_keys-2347073860
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("alanila/autotrain-acc_keys-2347073860", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("alanila/autotrain-acc_keys-2347073860", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```