---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Luojike/autotrain-data-test-4-macbert
co2_eq_emissions: 0.012225117907336358
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1071837613
- CO2 Emissions (in grams): 0.012225117907336358

## Validation Metrics

- Loss: 0.533202052116394
- Accuracy: 0.7408088235294118
- Precision: 0.5072463768115942
- Recall: 0.4088785046728972
- AUC: 0.710585043624057
- F1: 0.4527813712807245

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Luojike/autotrain-test-4-macbert-1071837613
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Luojike/autotrain-test-4-macbert-1071837613", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Luojike/autotrain-test-4-macbert-1071837613", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```