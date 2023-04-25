---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- LiveEvil/autotrain-data-copuml-la-beta-demo
co2_eq_emissions:
  emissions: 1.2815143214785873
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2205770755
- CO2 Emissions (in grams): 1.2815

## Validation Metrics

- Loss: 1.085
- Accuracy: 0.747
- Macro F1: 0.513
- Micro F1: 0.747
- Weighted F1: 0.715
- Macro Precision: 0.533
- Micro Precision: 0.747
- Weighted Precision: 0.691
- Macro Recall: 0.515
- Micro Recall: 0.747
- Weighted Recall: 0.747


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/LiveEvil/autotrain-copuml-la-beta-demo-2205770755
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("LiveEvil/autotrain-copuml-la-beta-demo-2205770755", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("LiveEvil/autotrain-copuml-la-beta-demo-2205770755", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```