---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "مطر غزير على شوارع العاصمة المقدسة."
datasets:
- MMars/autotrain-data-arabertv2_flodusta
co2_eq_emissions:
  emissions: 3.6263155149619304
---
# Labels Mapping
0 non event 

1 flood 

2 dust storm 

3 traffic accident


# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2782582128
- CO2 Emissions (in grams): 3.6263

## Validation Metrics

- Loss: 0.144
- Accuracy: 0.953
- Macro F1: 0.951
- Micro F1: 0.953
- Weighted F1: 0.953
- Macro Precision: 0.951
- Micro Precision: 0.953
- Weighted Precision: 0.953
- Macro Recall: 0.952
- Micro Recall: 0.953
- Weighted Recall: 0.953


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/MMars/autotrain-arabertv2_flodusta-2782582128
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("MMars/arabertv2_flodusta", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("MMars/arabertv2_flodusta", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```