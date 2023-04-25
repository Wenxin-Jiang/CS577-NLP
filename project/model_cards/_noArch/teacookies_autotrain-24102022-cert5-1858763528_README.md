---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-24102022-cert5
co2_eq_emissions:
  emissions: 15.97111881210848
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1858763528
- CO2 Emissions (in grams): 15.9711

## Validation Metrics

- Loss: 0.003
- Accuracy: 0.999
- Precision: 0.961
- Recall: 0.970
- F1: 0.966

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-24102022-cert5-1858763528
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-24102022-cert5-1858763528", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-24102022-cert5-1858763528", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```