---
tags:
- autotrain
- token-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- ankleBowl/autotrain-data-lucy-song-request
co2_eq_emissions:
  emissions: 1.0504382303760451
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1537055286
- CO2 Emissions (in grams): 1.0504

## Validation Metrics

- Loss: 0.014
- Accuracy: 0.997
- Precision: 0.997
- Recall: 0.997
- F1: 0.997

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/ankleBowl/autotrain-lucy-song-request-1537055286
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("ankleBowl/autotrain-lucy-song-request-1537055286", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("ankleBowl/autotrain-lucy-song-request-1537055286", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```