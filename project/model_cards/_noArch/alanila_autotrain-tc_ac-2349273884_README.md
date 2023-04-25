---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- alanila/autotrain-data-tc_ac
co2_eq_emissions:
  emissions: 1.196433244085964
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2349273884
- CO2 Emissions (in grams): 1.1964

## Validation Metrics

- Loss: 1.271
- Accuracy: 0.517
- Macro F1: 0.465
- Micro F1: 0.517
- Weighted F1: 0.437
- Macro Precision: 0.495
- Micro Precision: 0.517
- Weighted Precision: 0.488
- Macro Recall: 0.501
- Micro Recall: 0.517
- Weighted Recall: 0.517


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/alanila/autotrain-tc_ac-2349273884
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("alanila/autotrain-tc_ac-2349273884", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("alanila/autotrain-tc_ac-2349273884", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```