---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- DingYao/autotrain-data-fbert-singlish
co2_eq_emissions:
  emissions: 1.3946229895659434
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1755361190
- CO2 Emissions (in grams): 1.3946

## Validation Metrics

- Loss: 0.399
- Accuracy: 0.843
- Macro F1: 0.832
- Micro F1: 0.843
- Weighted F1: 0.844
- Macro Precision: 0.818
- Micro Precision: 0.843
- Weighted Precision: 0.848
- Macro Recall: 0.849
- Micro Recall: 0.843
- Weighted Recall: 0.843


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/DingYao/autotrain-fbert-singlish-1755361190
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("DingYao/autotrain-fbert-singlish-1755361190", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("DingYao/autotrain-fbert-singlish-1755361190", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```