---
tags:
- autotrain
- text-classification
language:
- it
widget:
- text: "I love AutoTrain 🤗"
datasets:
- micole66/autotrain-data-strano-o-normale
co2_eq_emissions:
  emissions: 0.6330824015396253
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1798362191
- CO2 Emissions (in grams): 0.6331

## Validation Metrics

- Loss: 0.645
- Accuracy: 0.750
- Precision: 1.000
- Recall: 0.500
- AUC: 0.625
- F1: 0.667

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/micole66/autotrain-strano-o-normale-1798362191
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("micole66/autotrain-strano-o-normale-1798362191", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("micole66/autotrain-strano-o-normale-1798362191", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```