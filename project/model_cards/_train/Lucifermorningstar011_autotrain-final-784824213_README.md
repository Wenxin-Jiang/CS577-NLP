---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Lucifermorningstar011/autotrain-data-final
co2_eq_emissions: 443.62532415086787
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 784824213
- CO2 Emissions (in grams): 443.62532415086787

## Validation Metrics

- Loss: 0.12777526676654816
- Accuracy: 0.9823625038850627
- Precision: 0.0
- Recall: 0.0
- F1: 0.0

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Lucifermorningstar011/autotrain-final-784824213
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Lucifermorningstar011/autotrain-final-784824213", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Lucifermorningstar011/autotrain-final-784824213", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```