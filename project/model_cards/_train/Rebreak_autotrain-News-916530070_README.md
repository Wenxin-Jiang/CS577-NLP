---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Rebreak/autotrain-data-News
co2_eq_emissions: 62.61326668998836
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 916530070
- CO2 Emissions (in grams): 62.61326668998836

## Validation Metrics

- Loss: 0.0855042040348053
- Accuracy: 0.9773220921733938
- Precision: 0.673469387755102
- Recall: 0.014864864864864866
- AUC: 0.8605107881181646
- F1: 0.029087703834288235

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Rebreak/autotrain-News-916530070
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Rebreak/autotrain-News-916530070", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Rebreak/autotrain-News-916530070", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```