---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Akhror/autotrain-data-text-classification-kunuz
co2_eq_emissions:
  emissions: 22.431314788743986
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1630257501
- CO2 Emissions (in grams): 22.4313

## Validation Metrics

- Loss: 0.975
- Accuracy: 0.647
- Macro F1: 0.542
- Micro F1: 0.647
- Weighted F1: 0.629
- Macro Precision: 0.534
- Micro Precision: 0.647
- Weighted Precision: 0.616
- Macro Recall: 0.558
- Micro Recall: 0.647
- Weighted Recall: 0.647


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Akhror/autotrain-text-classification-kunuz-1630257501
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Akhror/autotrain-text-classification-kunuz-1630257501", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Akhror/autotrain-text-classification-kunuz-1630257501", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```