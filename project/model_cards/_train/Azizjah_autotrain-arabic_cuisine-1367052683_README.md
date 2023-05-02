---
tags:
- autotrain
- text-classification
language:
- ar
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Azizjah/autotrain-data-arabic_cuisine
co2_eq_emissions:
  emissions: 0.02430968865158923
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1367052683
- CO2 Emissions (in grams): 0.0243

## Validation Metrics

- Loss: 2.302
- Accuracy: 0.439
- Macro F1: 0.133
- Micro F1: 0.439
- Weighted F1: 0.391
- Macro Precision: 0.167
- Micro Precision: 0.439
- Weighted Precision: 0.378
- Macro Recall: 0.140
- Micro Recall: 0.439
- Weighted Recall: 0.439


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Azizjah/autotrain-arabic_cuisine-1367052683
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Azizjah/autotrain-arabic_cuisine-1367052683", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Azizjah/autotrain-arabic_cuisine-1367052683", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```