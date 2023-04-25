---
tags:
- autotrain
- token-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- deepaksiloka/autotrain-data-name_classification
co2_eq_emissions:
  emissions: 0.3857777634696358
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1685059436
- CO2 Emissions (in grams): 0.3858

## Validation Metrics

- Loss: 0.063
- Accuracy: 0.988
- Precision: 0.989
- Recall: 0.989
- F1: 0.989

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/deepaksiloka/autotrain-name_classification-1685059436
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("deepaksiloka/autotrain-name_classification-1685059436", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("deepaksiloka/autotrain-name_classification-1685059436", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```