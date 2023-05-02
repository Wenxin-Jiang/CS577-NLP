---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- BenWord/autotrain-data-APMv2Multiclass
co2_eq_emissions:
  emissions: 2.4364900803769225
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1216046004
- CO2 Emissions (in grams): 2.4365

## Validation Metrics

- Loss: 0.094
- Accuracy: 1.000
- Macro F1: 1.000
- Micro F1: 1.000
- Weighted F1: 1.000
- Macro Precision: 1.000
- Micro Precision: 1.000
- Weighted Precision: 1.000
- Macro Recall: 1.000
- Micro Recall: 1.000
- Weighted Recall: 1.000


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/BenWord/autotrain-APMv2Multiclass-1216046004
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("BenWord/autotrain-APMv2Multiclass-1216046004", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("BenWord/autotrain-APMv2Multiclass-1216046004", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```