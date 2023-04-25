---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-25102022-cert2
co2_eq_emissions:
  emissions: 23.303137544479885
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1871863945
- CO2 Emissions (in grams): 23.3031

## Validation Metrics

- Loss: 0.002
- Accuracy: 1.000
- Precision: 0.984
- Recall: 0.986
- F1: 0.985

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-25102022-cert2-1871863945
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-25102022-cert2-1871863945", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-25102022-cert2-1871863945", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```