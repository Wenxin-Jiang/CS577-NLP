---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- davanstrien/autotrain-data-recipes
co2_eq_emissions:
  emissions: 9.62915730999643
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2451975972
- CO2 Emissions (in grams): 9.6292

## Validation Metrics

- Loss: 0.053
- Accuracy: 0.989
- Macro F1: 0.933
- Micro F1: 0.989
- Weighted F1: 0.989
- Macro Precision: 0.941
- Micro Precision: 0.989
- Weighted Precision: 0.989
- Macro Recall: 0.926
- Micro Recall: 0.989
- Weighted Recall: 0.989


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/davanstrien/autotrain-recipes-2451975972
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("davanstrien/autotrain-recipes-2451975972", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("davanstrien/autotrain-recipes-2451975972", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```