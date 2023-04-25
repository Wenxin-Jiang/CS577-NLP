---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- YilinWang42/autotrain-data-trial-run
co2_eq_emissions:
  emissions: 0.00977392698077684
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1444253725
- CO2 Emissions (in grams): 0.0098

## Validation Metrics

- Loss: 0.082
- Accuracy: 0.980
- Precision: 0.743
- Recall: 0.778
- F1: 0.760

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/YilinWang42/autotrain-trial-run-1444253725
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("YilinWang42/autotrain-trial-run-1444253725", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("YilinWang42/autotrain-trial-run-1444253725", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```