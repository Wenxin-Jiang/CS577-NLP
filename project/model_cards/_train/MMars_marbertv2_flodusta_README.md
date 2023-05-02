---
tags:
- autotrain
- text-classification
language:
- ar
widget:
- text: مطر غزير على شوارع العاصمة المقدسة.
datasets:
- MMars/autotrain-data-marbertv2_flodusta
co2_eq_emissions:
  emissions: 0.026171515160105633
metrics:
- accuracy
- precision
- recall
- f1
---
# Labels Mapping
0 non event 

1 flood 

2 dust storm 

3 traffic accident


# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2782682135
- CO2 Emissions (in grams): 0.0262

## Validation Metrics

- Loss: 0.157
- Accuracy: 0.948
- Macro F1: 0.945
- Micro F1: 0.948
- Weighted F1: 0.948
- Macro Precision: 0.940
- Micro Precision: 0.948
- Weighted Precision: 0.949
- Macro Recall: 0.952
- Micro Recall: 0.948
- Weighted Recall: 0.948


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/MMars/autotrain-marbertv2_flodusta-2782682135
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("MMars/marbertv2_flodusta", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("MMars/marbertv2_flodusta", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```