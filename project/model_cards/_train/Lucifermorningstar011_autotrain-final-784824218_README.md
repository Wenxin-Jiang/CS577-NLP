---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Lucifermorningstar011/autotrain-data-final
co2_eq_emissions: 237.58504390669626
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 784824218
- CO2 Emissions (in grams): 237.58504390669626

## Validation Metrics

- Loss: 0.2379177361726761
- Accuracy: 0.9734973172736223
- Precision: 0.0
- Recall: 0.0
- F1: 0.0

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Lucifermorningstar011/autotrain-final-784824218
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Lucifermorningstar011/autotrain-final-784824218", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Lucifermorningstar011/autotrain-final-784824218", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```