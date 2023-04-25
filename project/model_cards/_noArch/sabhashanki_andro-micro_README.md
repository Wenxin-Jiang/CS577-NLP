---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
- inference : true
datasets:
- sabhashanki/autotrain-data-micro-dataset-text-classification
co2_eq_emissions:
  emissions: 2.843258817349137
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2499077017
- CO2 Emissions (in grams): 2.8433

## Validation Metrics

- Loss: 0.366
- Accuracy: 0.901
- Macro F1: 0.897
- Micro F1: 0.901
- Weighted F1: 0.901
- Macro Precision: 0.914
- Micro Precision: 0.901
- Weighted Precision: 0.907
- Macro Recall: 0.888
- Micro Recall: 0.901
- Weighted Recall: 0.901


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/sabhashanki/autotrain-micro-dataset-text-classification-2499077017
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("sabhashanki/autotrain-micro-dataset-text-classification-2499077017", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("sabhashanki/autotrain-micro-dataset-text-classification-2499077017", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```