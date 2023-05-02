---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Luojike/autotrain-data-test_3
co2_eq_emissions: 0.03985401798934018
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1071537591
- CO2 Emissions (in grams): 0.03985401798934018

## Validation Metrics

- Loss: 0.5283975601196289
- Accuracy: 0.7389705882352942
- Precision: 0.5032894736842105
- Recall: 0.3574766355140187
- AUC: 0.7135599403856304
- F1: 0.41803278688524587

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Luojike/autotrain-test_3-1071537591
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Luojike/autotrain-test_3-1071537591", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Luojike/autotrain-test_3-1071537591", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```