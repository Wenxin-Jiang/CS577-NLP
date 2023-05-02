---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- PhucLe/autotrain-data-LRO-tratify-data
co2_eq_emissions:
  emissions: 2.223269909428516
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1237947025
- CO2 Emissions (in grams): 2.2233

## Validation Metrics

- Loss: 0.392
- Accuracy: 0.869
- Macro F1: 0.868
- Micro F1: 0.869
- Weighted F1: 0.868
- Macro Precision: 0.871
- Micro Precision: 0.869
- Weighted Precision: 0.871
- Macro Recall: 0.869
- Micro Recall: 0.869
- Weighted Recall: 0.869


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/PhucLe/autotrain-LRO-tratify-data-1237947025
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("PhucLe/autotrain-LRO-tratify-data-1237947025", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("PhucLe/autotrain-LRO-tratify-data-1237947025", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```