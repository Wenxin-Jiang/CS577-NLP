---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- bggmyfuture-ai/autotrain-data-sphere-intent-classification
co2_eq_emissions:
  emissions: 1.893124351907886
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1584456046
- CO2 Emissions (in grams): 1.8931

## Validation Metrics

- Loss: 0.690
- Accuracy: 0.744
- Macro F1: 0.678
- Micro F1: 0.744
- Weighted F1: 0.739
- Macro Precision: 0.697
- Micro Precision: 0.744
- Weighted Precision: 0.738
- Macro Recall: 0.669
- Micro Recall: 0.744
- Weighted Recall: 0.744


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/bggmyfuture-ai/autotrain-sphere-intent-classification-1584456046
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("bggmyfuture-ai/autotrain-sphere-intent-classification-1584456046", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("bggmyfuture-ai/autotrain-sphere-intent-classification-1584456046", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```