---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-17102022-update_scope_and_date
co2_eq_emissions:
  emissions: 19.692537664708304
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1789062099
- CO2 Emissions (in grams): 19.6925

## Validation Metrics

- Loss: 0.029
- Accuracy: 0.992
- Precision: 0.777
- Recall: 0.826
- F1: 0.801

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-17102022-update_scope_and_date-1789062099
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-17102022-update_scope_and_date-1789062099", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-17102022-update_scope_and_date-1789062099", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```