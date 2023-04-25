---
tags:
- autotrain
- text-classification
language:
- zh
widget:
- text: "I love AutoTrain 🤗"
datasets:
- paulkm/autotrain-data-lottery_v2
co2_eq_emissions:
  emissions: 0.06047934032845949
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2420075389
- CO2 Emissions (in grams): 0.0605

## Validation Metrics

- Loss: 0.122
- Accuracy: 0.965
- Precision: 0.976
- Recall: 0.946
- AUC: 0.988
- F1: 0.961

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/paulkm/autotrain-lottery_v2-2420075389
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("paulkm/autotrain-lottery_v2-2420075389", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("paulkm/autotrain-lottery_v2-2420075389", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```