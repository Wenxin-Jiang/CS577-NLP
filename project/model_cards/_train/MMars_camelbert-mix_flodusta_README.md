---
tags:
- autotrain
- text-classification
language:
- ar
widget:
- text: مطر غزير على شوارع العاصمة المقدسة.
datasets:
- MMars/autotrain-data-camelbert-mix_flodusta
co2_eq_emissions:
  emissions: 0.010214592292905006
metrics:
- accuracy
- f1
- precision
- recall
---
# Labels Mapping
0 non event 

1 flood 

2 dust storm 

3 traffic accident


# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2783082152
- CO2 Emissions (in grams): 0.0102

## Validation Metrics

- Loss: 0.149
- Accuracy: 0.949
- Macro F1: 0.946
- Micro F1: 0.949
- Weighted F1: 0.949
- Macro Precision: 0.942
- Micro Precision: 0.949
- Weighted Precision: 0.950
- Macro Recall: 0.951
- Micro Recall: 0.949
- Weighted Recall: 0.949


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/MMars/autotrain-camelbert-mix_flodusta-2783082152
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("MMars/camelbert-mix_flodusta", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("MMars/camelbert-mix_flodusta", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```