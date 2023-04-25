---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- hoshingakag/autotrain-data-emotion-detection
co2_eq_emissions:
  emissions: 2.3491292126039087
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1587956110
- CO2 Emissions (in grams): 2.3491

## Validation Metrics

- Loss: 0.448
- Accuracy: 0.888
- Macro F1: 0.823
- Micro F1: 0.888
- Weighted F1: 0.884
- Macro Precision: 0.885
- Micro Precision: 0.888
- Weighted Precision: 0.890
- Macro Recall: 0.800
- Micro Recall: 0.888
- Weighted Recall: 0.888


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/hoshingakag/autotrain-emotion-detection-1587956110
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("hoshingakag/autotrain-emotion-detection-1587956110", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("hoshingakag/autotrain-emotion-detection-1587956110", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```