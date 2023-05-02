---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Maxbnza/autotrain-data-address-training
co2_eq_emissions: 141.11976199388627
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1062136864
- CO2 Emissions (in grams): 141.11976199388627

## Validation Metrics

- Loss: 0.10147109627723694
- Accuracy: 0.9859325979151907
- Macro F1: 0.9715036017680622
- Micro F1: 0.9859325979151907
- Weighted F1: 0.9859070541468058
- Macro Precision: 0.9732956651937184
- Micro Precision: 0.9859325979151907
- Weighted Precision: 0.9860574596777458
- Macro Recall: 0.970199341807239
- Micro Recall: 0.9859325979151907
- Weighted Recall: 0.9859325979151907


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Maxbnza/autotrain-address-training-1062136864
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Maxbnza/autotrain-address-training-1062136864", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Maxbnza/autotrain-address-training-1062136864", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```