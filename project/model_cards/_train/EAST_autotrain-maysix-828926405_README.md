---
tags: autotrain
language: zh
widget:
- text: "I love AutoTrain 🤗"
datasets:
- EAST/autotrain-data-maysix
co2_eq_emissions: 0.00258669198292644
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 828926405
- CO2 Emissions (in grams): 0.00258669198292644

## Validation Metrics

- Loss: 0.1797131597995758
- Accuracy: 0.9318181818181818
- Precision: 0.9047619047619048
- Recall: 0.95
- AUC: 0.9875
- F1: 0.9268292682926829

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/EAST/autotrain-maysix-828926405
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("EAST/autotrain-maysix-828926405", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("EAST/autotrain-maysix-828926405", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```