---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- DingYao/autotrain-data-fbert-singlish-5
co2_eq_emissions:
  emissions: 2.1095744631067883
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1943965533
- CO2 Emissions (in grams): 2.1096

## Validation Metrics

- Loss: 0.310
- Accuracy: 0.880
- Macro F1: 0.766
- Micro F1: 0.880
- Weighted F1: 0.877
- Macro Precision: 0.826
- Micro Precision: 0.880
- Weighted Precision: 0.877
- Macro Recall: 0.735
- Micro Recall: 0.880
- Weighted Recall: 0.880


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/DingYao/autotrain-fbert-singlish-5-1943965533
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("DingYao/autotrain-fbert-singlish-5-1943965533", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("DingYao/autotrain-fbert-singlish-5-1943965533", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```