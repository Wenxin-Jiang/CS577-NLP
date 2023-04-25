---
tags:
- autotrain
- token-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- deepaksiloka/autotrain-data-name_classification_3
co2_eq_emissions:
  emissions: 1.0819688360882111
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1686659457
- CO2 Emissions (in grams): 1.0820

## Validation Metrics

- Loss: 0.087
- Accuracy: 0.978
- Precision: 0.979
- Recall: 0.987
- F1: 0.983

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/deepaksiloka/autotrain-name_classification_3-1686659457
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("deepaksiloka/autotrain-name_classification_3-1686659457", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("deepaksiloka/autotrain-name_classification_3-1686659457", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```