---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- kroos/autotrain-data-book_recommender
co2_eq_emissions:
  emissions: 10.620169750625415
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1867863842
- CO2 Emissions (in grams): 10.6202

## Validation Metrics

- Loss: 0.946
- Accuracy: 0.594
- Macro F1: 0.387
- Micro F1: 0.594
- Weighted F1: 0.574
- Macro Precision: 0.370
- Micro Precision: 0.594
- Weighted Precision: 0.567
- Macro Recall: 0.417
- Micro Recall: 0.594
- Weighted Recall: 0.594


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/kroos/autotrain-book_recommender-1867863842
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("kroos/autotrain-book_recommender-1867863842", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("kroos/autotrain-book_recommender-1867863842", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```