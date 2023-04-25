---
tags:
- autotrain
- token-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Olusegun/autotrain-data-disease_tokens
co2_eq_emissions:
  emissions: 1.569698418187329
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2095367455
- CO2 Emissions (in grams): 1.5697

## Validation Metrics

- Loss: 0.000
- Accuracy: 1.000
- Precision: 1.000
- Recall: 1.000
- F1: 1.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Olusegun/autotrain-disease_tokens-2095367455
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Olusegun/autotrain-disease_tokens-2095367455", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Olusegun/autotrain-disease_tokens-2095367455", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```