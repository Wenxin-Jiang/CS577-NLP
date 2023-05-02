---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Shenzy2/autotrain-data-tk
co2_eq_emissions: 0.004663044473485149
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1181244086
- CO2 Emissions (in grams): 0.004663044473485149

## Validation Metrics

- Loss: 0.5532978773117065
- Accuracy: 0.8263097949886105
- Precision: 0.5104166666666666
- Recall: 0.4681528662420382
- F1: 0.4883720930232558

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Shenzy2/autotrain-tk-1181244086
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Shenzy2/autotrain-tk-1181244086", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Shenzy2/autotrain-tk-1181244086", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```