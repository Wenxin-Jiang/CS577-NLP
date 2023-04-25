---
tags:
- autotrain
- token-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- micole66/autotrain-data-pachyderm
co2_eq_emissions:
  emissions: 1.2406150246482144
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1799762243
- CO2 Emissions (in grams): 1.2406

## Validation Metrics

- Loss: 0.463
- Accuracy: 1.000
- Precision: 1.000
- Recall: 1.000
- F1: 1.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/micole66/autotrain-pachyderm-1799762243
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("micole66/autotrain-pachyderm-1799762243", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("micole66/autotrain-pachyderm-1799762243", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```