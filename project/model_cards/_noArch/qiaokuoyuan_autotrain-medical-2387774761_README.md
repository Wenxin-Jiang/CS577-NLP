---
tags:
- autotrain
- token-classification
language:
- zh
widget:
- text: "I love AutoTrain 🤗"
datasets:
- qiaokuoyuan/autotrain-data-medical-cfa966ee
co2_eq_emissions:
  emissions: 0.7237073793849912
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2387774761
- CO2 Emissions (in grams): 0.7237

## Validation Metrics

- Loss: 0.032
- Accuracy: 0.990
- Precision: 0.000
- Recall: 0.000
- F1: 0.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/qiaokuoyuan/autotrain-medical-2387774761
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("qiaokuoyuan/autotrain-medical-2387774761", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("qiaokuoyuan/autotrain-medical-2387774761", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```