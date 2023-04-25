---
tags:
- autotrain
- text-classification
language:
- pt
widget:
- text: "I love AutoTrain 🤗"
datasets:
- lehomme/autotrain-data-pruebaa
co2_eq_emissions:
  emissions: 0.017706430838852625
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1470254048
- CO2 Emissions (in grams): 0.0177

## Validation Metrics

- Loss: 0.637
- Accuracy: 0.738
- Macro F1: 0.739
- Micro F1: 0.738
- Weighted F1: 0.739
- Macro Precision: 0.744
- Micro Precision: 0.738
- Weighted Precision: 0.744
- Macro Recall: 0.738
- Micro Recall: 0.738
- Weighted Recall: 0.738


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/lehomme/autotrain-pruebaa-1470254048
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("lehomme/autotrain-pruebaa-1470254048", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("lehomme/autotrain-pruebaa-1470254048", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```