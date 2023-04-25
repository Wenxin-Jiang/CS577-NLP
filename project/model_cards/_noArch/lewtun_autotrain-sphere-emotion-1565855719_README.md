---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- lewtun/autotrain-data-sphere-emotion
co2_eq_emissions:
  emissions: 0.02429248200067234
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1565855719
- CO2 Emissions (in grams): 0.0243

## Validation Metrics

- Loss: 0.134
- Accuracy: 0.943
- Macro F1: 0.915
- Micro F1: 0.943
- Weighted F1: 0.943
- Macro Precision: 0.911
- Micro Precision: 0.943
- Weighted Precision: 0.943
- Macro Recall: 0.920
- Micro Recall: 0.943
- Weighted Recall: 0.943


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/lewtun/autotrain-sphere-emotion-1565855719
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("lewtun/autotrain-sphere-emotion-1565855719", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("lewtun/autotrain-sphere-emotion-1565855719", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```