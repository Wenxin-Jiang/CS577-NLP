---
tags:
- autotrain
- token-classification
language:
- zh
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Kunologist/autotrain-data-nav-chinese
co2_eq_emissions:
  emissions: 2.1130584322221275
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2795482484
- CO2 Emissions (in grams): 2.1131

## Validation Metrics

- Loss: 0.020
- Accuracy: 0.998
- Precision: 0.984
- Recall: 0.984
- F1: 0.984

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Kunologist/autotrain-nav-chinese-2795482484
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Kunologist/autotrain-nav-chinese-2795482484", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Kunologist/autotrain-nav-chinese-2795482484", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```