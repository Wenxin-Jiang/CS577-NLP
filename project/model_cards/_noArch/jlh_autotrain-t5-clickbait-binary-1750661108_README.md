---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- jlh/autotrain-data-t5-clickbait-binary
co2_eq_emissions:
  emissions: 8.44003619525122
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1750661108
- CO2 Emissions (in grams): 8.4400

## Validation Metrics

- Loss: 0.006
- Accuracy: 0.998
- Precision: 0.998
- Recall: 0.999
- AUC: 1.000
- F1: 0.999

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/jlh/autotrain-t5-clickbait-binary-1750661108
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("jlh/autotrain-t5-clickbait-binary-1750661108", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("jlh/autotrain-t5-clickbait-binary-1750661108", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```