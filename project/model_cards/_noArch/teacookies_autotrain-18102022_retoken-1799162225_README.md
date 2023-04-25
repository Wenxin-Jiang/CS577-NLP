---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-18102022_retoken
co2_eq_emissions:
  emissions: 20.17997164723111
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1799162225
- CO2 Emissions (in grams): 20.1800

## Validation Metrics

- Loss: 0.024
- Accuracy: 0.993
- Precision: 0.829
- Recall: 0.893
- F1: 0.860

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-18102022_retoken-1799162225
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-18102022_retoken-1799162225", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-18102022_retoken-1799162225", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```