---
tags:
- autotrain
- token-classification
language:
- pt
widget:
- text: "I love AutoTrain 🤗"
datasets:
- famube/autotrain-data-documentos-oficiais
co2_eq_emissions:
  emissions: 6.461431564881563
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2092367351
- CO2 Emissions (in grams): 6.4614

## Validation Metrics

- Loss: 0.059
- Accuracy: 0.986
- Precision: 0.000
- Recall: 0.000
- F1: 0.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/famube/autotrain-documentos-oficiais-2092367351
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("famube/autotrain-documentos-oficiais-2092367351", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("famube/autotrain-documentos-oficiais-2092367351", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```