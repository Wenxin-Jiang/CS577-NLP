---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- CH0KUN/autotrain-data-TNC_Data2500_WangchanBERTa
co2_eq_emissions: 0.07293362913158113
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 928030564
- CO2 Emissions (in grams): 0.07293362913158113

## Validation Metrics

- Loss: 0.4989683926105499
- Accuracy: 0.8445845697329377
- Macro F1: 0.8407629450432429
- Micro F1: 0.8445845697329377
- Weighted F1: 0.8407629450432429
- Macro Precision: 0.8390327354531153
- Micro Precision: 0.8445845697329377
- Weighted Precision: 0.8390327354531154
- Macro Recall: 0.8445845697329377
- Micro Recall: 0.8445845697329377
- Weighted Recall: 0.8445845697329377


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/CH0KUN/autotrain-TNC_Data2500_WangchanBERTa-928030564
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("CH0KUN/autotrain-TNC_Data2500_WangchanBERTa-928030564", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("CH0KUN/autotrain-TNC_Data2500_WangchanBERTa-928030564", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```