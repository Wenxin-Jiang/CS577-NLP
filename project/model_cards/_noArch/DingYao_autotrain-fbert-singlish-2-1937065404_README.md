---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- DingYao/autotrain-data-fbert-singlish-2
co2_eq_emissions:
  emissions: 1.04277637543434
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1937065404
- CO2 Emissions (in grams): 1.0428

## Validation Metrics

- Loss: 0.368
- Accuracy: 0.858
- Macro F1: 0.717
- Micro F1: 0.858
- Weighted F1: 0.857
- Macro Precision: 0.731
- Micro Precision: 0.858
- Weighted Precision: 0.859
- Macro Recall: 0.711
- Micro Recall: 0.858
- Weighted Recall: 0.858


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/DingYao/autotrain-fbert-singlish-2-1937065404
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("DingYao/autotrain-fbert-singlish-2-1937065404", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("DingYao/autotrain-fbert-singlish-2-1937065404", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```