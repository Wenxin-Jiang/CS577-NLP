---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- mrosinski/autotrain-data-distilbert-risk-ranker
co2_eq_emissions:
  emissions: 0.02016784254717722
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1593356256
- CO2 Emissions (in grams): 0.0202

## Validation Metrics

- Loss: 0.995
- Accuracy: 0.511
- Macro F1: 0.506
- Micro F1: 0.511
- Weighted F1: 0.506
- Macro Precision: 0.505
- Micro Precision: 0.511
- Weighted Precision: 0.505
- Macro Recall: 0.511
- Micro Recall: 0.511
- Weighted Recall: 0.511


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/mrosinski/autotrain-distilbert-risk-ranker-1593356256
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("mrosinski/autotrain-distilbert-risk-ranker-1593356256", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("mrosinski/autotrain-distilbert-risk-ranker-1593356256", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```