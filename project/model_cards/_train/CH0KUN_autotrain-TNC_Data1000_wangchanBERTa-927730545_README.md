---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- CH0KUN/autotrain-data-TNC_Data1000_wangchanBERTa
co2_eq_emissions: 0.03882318406133382
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 927730545
- CO2 Emissions (in grams): 0.03882318406133382

## Validation Metrics

- Loss: 0.346664160490036
- Accuracy: 0.9212962962962963
- Macro F1: 0.9193830593356196
- Micro F1: 0.9212962962962963
- Weighted F1: 0.9213272351125573
- Macro Precision: 0.920255423800781
- Micro Precision: 0.9212962962962963
- Weighted Precision: 0.9231182355921642
- Macro Recall: 0.920208415963133
- Micro Recall: 0.9212962962962963
- Weighted Recall: 0.9212962962962963


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/CH0KUN/autotrain-TNC_Data1000_wangchanBERTa-927730545
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("CH0KUN/autotrain-TNC_Data1000_wangchanBERTa-927730545", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("CH0KUN/autotrain-TNC_Data1000_wangchanBERTa-927730545", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```