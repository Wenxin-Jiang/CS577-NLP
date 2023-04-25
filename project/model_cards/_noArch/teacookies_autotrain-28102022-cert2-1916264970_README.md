---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-28102022-cert2
co2_eq_emissions:
  emissions: 17.982023070008026
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1916264970
- CO2 Emissions (in grams): 17.9820

## Validation Metrics

- Loss: 0.002
- Accuracy: 1.000
- Precision: 0.980
- Recall: 0.986
- F1: 0.983

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-28102022-cert2-1916264970
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-28102022-cert2-1916264970", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-28102022-cert2-1916264970", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```