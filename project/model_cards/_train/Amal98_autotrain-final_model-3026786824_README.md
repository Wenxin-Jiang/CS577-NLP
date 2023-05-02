---
tags:
- autotrain
- token-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Amal98/autotrain-data-final_model
co2_eq_emissions:
  emissions: 3.5122512070831804
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 3026786824
- CO2 Emissions (in grams): 3.5123

## Validation Metrics

- Loss: 0.221
- Accuracy: 0.940
- Precision: 0.557
- Recall: 0.509
- F1: 0.532

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Amal98/autotrain-final_model-3026786824
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Amal98/autotrain-final_model-3026786824", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Amal98/autotrain-final_model-3026786824", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```