---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "Shankesh designed this model from scratch 🤗"
datasets:
- sabhashanki/autotrain-data-khul-classify
co2_eq_emissions:
  emissions: 2.8092927891228863
inference: true
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2396974951
- CO2 Emissions (in grams): 2.8093

## Validation Metrics

- Loss: 0.635
- Accuracy: 0.840
- Macro F1: 0.834
- Micro F1: 0.840
- Weighted F1: 0.837
- Macro Precision: 0.839
- Micro Precision: 0.840
- Weighted Precision: 0.840
- Macro Recall: 0.836
- Micro Recall: 0.840
- Weighted Recall: 0.840


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/sabhashanki/autotrain-topic-prediction-latest-2396974951
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("sabhashanki/autotrain-topic-prediction-latest-2396974951", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("sabhashanki/autotrain-topic-prediction-latest-2396974951", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```