---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Sathira/autotrain-data-mbtiNlp
co2_eq_emissions: 121.67185089502216
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 798824628
- CO2 Emissions (in grams): 121.67185089502216

## Validation Metrics

- Loss: 0.5046824812889099
- Accuracy: 0.8472124039775673
- Macro F1: 0.7812978033330673
- Micro F1: 0.8472124039775673
- Weighted F1: 0.8464983956259307
- Macro Precision: 0.812208631055716
- Micro Precision: 0.8472124039775673
- Weighted Precision: 0.8478968364150775
- Macro Recall: 0.7593223884993787
- Micro Recall: 0.8472124039775673
- Weighted Recall: 0.8472124039775673


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Sathira/autotrain-mbtiNlp-798824628
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Sathira/autotrain-mbtiNlp-798824628", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Sathira/autotrain-mbtiNlp-798824628", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```