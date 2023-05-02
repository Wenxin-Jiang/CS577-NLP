---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- LewisShanghai/autotrain-data-books-rating-analysis
co2_eq_emissions:
  emissions: 13.050690238461922
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2885184365
- CO2 Emissions (in grams): 13.0507

## Validation Metrics

- Loss: 0.797
- Accuracy: 0.652
- Macro F1: 0.425
- Micro F1: 0.652
- Weighted F1: 0.637
- Macro Precision: 0.396
- Micro Precision: 0.652
- Weighted Precision: 0.634
- Macro Recall: 0.478
- Micro Recall: 0.652
- Weighted Recall: 0.652


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/LewisShanghai/autotrain-books-rating-analysis-2885184365
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("LewisShanghai/autotrain-books-rating-analysis-2885184365", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("LewisShanghai/autotrain-books-rating-analysis-2885184365", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```