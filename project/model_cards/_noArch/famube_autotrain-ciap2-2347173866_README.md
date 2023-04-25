---
tags:
- autotrain
- text-classification
language:
- pt
widget:
- text: "febre"
- text: "dor de cabeça"
- text: "corpo inteiro doendo"
datasets:
- famube/autotrain-data-ciap2
co2_eq_emissions:
  emissions: 4.825567476024859
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2347173866
- CO2 Emissions (in grams): 4.8256

## Validation Metrics

- Loss: 1.932
- Accuracy: 0.681
- Macro F1: 0.609
- Micro F1: 0.681
- Weighted F1: 0.622
- Macro Precision: 0.592
- Micro Precision: 0.681
- Weighted Precision: 0.610
- Macro Recall: 0.669
- Micro Recall: 0.681
- Weighted Recall: 0.681


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/famube/autotrain-ciap2-2347173866
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("famube/autotrain-ciap2-2347173866", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("famube/autotrain-ciap2-2347173866", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```