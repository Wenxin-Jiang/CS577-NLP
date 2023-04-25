---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-17102022_modifty_split_func_cert
co2_eq_emissions:
  emissions: 0.07967502500155842
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1783761910
- CO2 Emissions (in grams): 0.0797

## Validation Metrics

- Loss: 0.017
- Accuracy: 0.995
- Precision: 0.850
- Recall: 0.884
- F1: 0.867

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-17102022_modifty_split_func_cert-1783761910
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-17102022_modifty_split_func_cert-1783761910", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-17102022_modifty_split_func_cert-1783761910", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```