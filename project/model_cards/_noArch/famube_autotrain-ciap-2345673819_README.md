---
tags:
- autotrain
- text-classification
language:
- pt
widget:
- text: ""
datasets:
- famube/autotrain-data-ciap
co2_eq_emissions:
  emissions: 4.04378848235129
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2345673819
- CO2 Emissions (in grams): 4.0438

## Validation Metrics

- Loss: 2.342
- Accuracy: 0.631
- Macro F1: 0.542
- Micro F1: 0.631
- Weighted F1: 0.546
- Macro Precision: 0.514
- Micro Precision: 0.631
- Weighted Precision: 0.515
- Macro Recall: 0.617
- Micro Recall: 0.631
- Weighted Recall: 0.631


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/famube/autotrain-ciap-2345673819
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("famube/autotrain-ciap-2345673819", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("famube/autotrain-ciap-2345673819", use_auth_token=True)

inputs = tokenizer("dor de cabeça", return_tensors="pt")

outputs = model(**inputs)
```