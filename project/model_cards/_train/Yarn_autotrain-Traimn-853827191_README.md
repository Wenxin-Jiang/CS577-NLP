---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Yarn/autotrain-data-Traimn
co2_eq_emissions: 1.712176860015081
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 853827191
- CO2 Emissions (in grams): 1.712176860015081

## Validation Metrics

- Loss: 0.10257730633020401
- Accuracy: 0.973421926910299
- Macro F1: 0.9735224586288418
- Micro F1: 0.973421926910299
- Weighted F1: 0.9735187934099364
- Macro Precision: 0.9738505933839127
- Micro Precision: 0.973421926910299
- Weighted Precision: 0.9738995774527256
- Macro Recall: 0.9734994306470444
- Micro Recall: 0.973421926910299
- Weighted Recall: 0.973421926910299


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Yarn/autotrain-Traimn-853827191
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Yarn/autotrain-Traimn-853827191", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Yarn/autotrain-Traimn-853827191", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```