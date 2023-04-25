---
tags:
- autotrain
- token-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Akshata/autotrain-data-person-name-validity1
co2_eq_emissions:
  emissions: 0.015012024821802214
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1655358687
- CO2 Emissions (in grams): 0.0150

## Validation Metrics

- Loss: 0.038
- Accuracy: 0.991
- Precision: 0.000
- Recall: 0.000
- F1: 0.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Akshata/autotrain-person-name-validity1-1655358687
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Akshata/autotrain-person-name-validity1-1655358687", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Akshata/autotrain-person-name-validity1-1655358687", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```