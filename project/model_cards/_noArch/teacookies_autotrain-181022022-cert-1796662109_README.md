---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-181022022-cert
co2_eq_emissions:
  emissions: 18.56487105177345
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1796662109
- CO2 Emissions (in grams): 18.5649

## Validation Metrics

- Loss: 0.029
- Accuracy: 0.991
- Precision: 0.767
- Recall: 0.813
- F1: 0.790

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-181022022-cert-1796662109
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-181022022-cert-1796662109", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-181022022-cert-1796662109", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```