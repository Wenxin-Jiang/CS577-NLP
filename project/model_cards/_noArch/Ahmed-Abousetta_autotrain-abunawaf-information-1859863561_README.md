---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Ahmed-Abousetta/autotrain-data-abunawaf-information
co2_eq_emissions:
  emissions: 1.5884381963682959
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1859863561
- CO2 Emissions (in grams): 1.5884

## Validation Metrics

- Loss: 0.338
- Accuracy: 0.869
- Precision: 0.836
- Recall: 0.868
- AUC: 0.932
- F1: 0.852

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ahmed-Abousetta/autotrain-abunawaf-information-1859863561
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-information-1859863561", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ahmed-Abousetta/autotrain-abunawaf-information-1859863561", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```