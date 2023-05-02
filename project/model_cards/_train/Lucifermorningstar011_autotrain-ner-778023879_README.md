---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Lucifermorningstar011/autotrain-data-ner
co2_eq_emissions: 43.26533004662002
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 778023879
- CO2 Emissions (in grams): 43.26533004662002

## Validation Metrics

- Loss: 5.475859779835446e-06
- Accuracy: 0.9999996519918594
- Precision: 0.0
- Recall: 0.0
- F1: 0.0

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Lucifermorningstar011/autotrain-ner-778023879
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Lucifermorningstar011/autotrain-ner-778023879", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Lucifermorningstar011/autotrain-ner-778023879", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```