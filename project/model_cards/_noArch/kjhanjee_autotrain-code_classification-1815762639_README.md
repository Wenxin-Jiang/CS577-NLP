---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- kjhanjee/autotrain-data-code_classification
co2_eq_emissions:
  emissions: 11.438220107218369
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1815762639
- CO2 Emissions (in grams): 11.4382

## Validation Metrics

- Loss: 0.849
- Accuracy: 0.794
- Macro F1: 0.788
- Micro F1: 0.794
- Weighted F1: 0.788
- Macro Precision: 0.797
- Micro Precision: 0.794
- Weighted Precision: 0.797
- Macro Recall: 0.794
- Micro Recall: 0.794
- Weighted Recall: 0.794


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/kjhanjee/autotrain-code_classification-1815762639
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("kjhanjee/autotrain-code_classification-1815762639", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("kjhanjee/autotrain-code_classification-1815762639", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```