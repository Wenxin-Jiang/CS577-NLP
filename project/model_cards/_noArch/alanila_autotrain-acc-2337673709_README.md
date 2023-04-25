---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- alanila/autotrain-data-acc
co2_eq_emissions:
  emissions: 1.6543357301983936
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2337673709
- CO2 Emissions (in grams): 1.6543

## Validation Metrics

- Loss: 1.331
- Accuracy: 0.492
- Macro F1: 0.457
- Micro F1: 0.492
- Weighted F1: 0.423
- Macro Precision: 0.464
- Micro Precision: 0.492
- Weighted Precision: 0.420
- Macro Recall: 0.484
- Micro Recall: 0.492
- Weighted Recall: 0.492


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/alanila/autotrain-acc-2337673709
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("alanila/autotrain-acc-2337673709", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("alanila/autotrain-acc-2337673709", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```