---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- prathap-reddy/autotrain-data-climate-text-classification
co2_eq_emissions:
  emissions: 2.621274122165296
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1437253674
- CO2 Emissions (in grams): 2.6213

## Validation Metrics

- Loss: 0.300
- Accuracy: 0.884
- Precision: 0.844
- Recall: 0.596
- AUC: 0.885
- F1: 0.699

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/prathap-reddy/autotrain-climate-text-classification-1437253674
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("prathap-reddy/autotrain-climate-text-classification-1437253674", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("prathap-reddy/autotrain-climate-text-classification-1437253674", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```