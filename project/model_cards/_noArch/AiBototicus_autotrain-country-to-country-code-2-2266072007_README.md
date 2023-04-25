---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- AiBototicus/autotrain-data-country-to-country-code-2
co2_eq_emissions:
  emissions: 0.023363865750613368
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2266072007
- CO2 Emissions (in grams): 0.0234

## Validation Metrics

- Loss: 0.556
- Accuracy: 0.940
- Macro F1: 0.741
- Micro F1: 0.940
- Weighted F1: 0.923
- Macro Precision: 0.732
- Micro Precision: 0.940
- Weighted Precision: 0.911
- Macro Recall: 0.759
- Micro Recall: 0.940
- Weighted Recall: 0.940


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/AiBototicus/autotrain-country-to-country-code-2-2266072007
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("AiBototicus/autotrain-country-to-country-code-2-2266072007", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("AiBototicus/autotrain-country-to-country-code-2-2266072007", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```