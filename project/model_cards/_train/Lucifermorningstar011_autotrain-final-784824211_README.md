---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Lucifermorningstar011/autotrain-data-final
co2_eq_emissions: 292.55119229577315
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 784824211
- CO2 Emissions (in grams): 292.55119229577315

## Validation Metrics

- Loss: 0.17682738602161407
- Accuracy: 0.9732196168090091
- Precision: 0.0
- Recall: 0.0
- F1: 0.0

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Lucifermorningstar011/autotrain-final-784824211
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Lucifermorningstar011/autotrain-final-784824211", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Lucifermorningstar011/autotrain-final-784824211", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```