---
tags:
- autotrain
- text-classification
inference: true
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- sabhashanki/autotrain-data-topic-prediction-latest
co2_eq_emissions:
  emissions: 2.0293128025440454
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2396974952
- CO2 Emissions (in grams): 2.0293

## Validation Metrics

- Loss: 0.656
- Accuracy: 0.846
- Macro F1: 0.826
- Micro F1: 0.846
- Weighted F1: 0.842
- Macro Precision: 0.867
- Micro Precision: 0.846
- Weighted Precision: 0.861
- Macro Recall: 0.829
- Micro Recall: 0.846
- Weighted Recall: 0.846


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/sabhashanki/autotrain-topic-prediction-latest-2396974952
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("sabhashanki/autotrain-topic-prediction-latest-2396974952", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("sabhashanki/autotrain-topic-prediction-latest-2396974952", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```