---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- sairahul5223/autotrain-data-auto-train-intent-classification-20220928
co2_eq_emissions:
  emissions: 1.0197546564964108
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1584756071
- CO2 Emissions (in grams): 1.0198

## Validation Metrics

- Loss: 0.764
- Accuracy: 0.666
- Macro F1: 0.618
- Micro F1: 0.666
- Weighted F1: 0.658
- Macro Precision: 0.659
- Micro Precision: 0.666
- Weighted Precision: 0.664
- Macro Recall: 0.604
- Micro Recall: 0.666
- Weighted Recall: 0.666


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/sairahul5223/autotrain-auto-train-intent-classification-20220928-1584756071
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("sairahul5223/autotrain-auto-train-intent-classification-20220928-1584756071", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("sairahul5223/autotrain-auto-train-intent-classification-20220928-1584756071", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```