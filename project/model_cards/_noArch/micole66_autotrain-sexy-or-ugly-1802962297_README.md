---
tags:
- autotrain
- token-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- micole66/autotrain-data-sexy-or-ugly
co2_eq_emissions:
  emissions: 0.316594943692132
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1802962297
- CO2 Emissions (in grams): 0.3166

## Validation Metrics

- Loss: 0.616
- Accuracy: 0.800
- Precision: 0.429
- Recall: 0.600
- F1: 0.500

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/micole66/autotrain-sexy-or-ugly-1802962297
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("micole66/autotrain-sexy-or-ugly-1802962297", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("micole66/autotrain-sexy-or-ugly-1802962297", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```