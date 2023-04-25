---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- fernanda-dionello/autotrain-data-autotrain_goodreads_string
co2_eq_emissions:
  emissions: 0.04700680417595474
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2164069744
- CO2 Emissions (in grams): 0.0470

## Validation Metrics

- Loss: 0.806
- Accuracy: 0.686
- Macro F1: 0.534
- Micro F1: 0.686
- Weighted F1: 0.678
- Macro Precision: 0.524
- Micro Precision: 0.686
- Weighted Precision: 0.673
- Macro Recall: 0.551
- Micro Recall: 0.686
- Weighted Recall: 0.686


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/fernanda-dionello/autotrain-autotrain_goodreads_string-2164069744
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("fernanda-dionello/autotrain-autotrain_goodreads_string-2164069744", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("fernanda-dionello/autotrain-autotrain_goodreads_string-2164069744", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```