---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-17102022_change_modlel
co2_eq_emissions:
  emissions: 22.12649933027385
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1783861900
- CO2 Emissions (in grams): 22.1265

## Validation Metrics

- Loss: 0.025
- Accuracy: 0.994
- Precision: 0.859
- Recall: 0.883
- F1: 0.871

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-17102022_change_modlel-1783861900
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-17102022_change_modlel-1783861900", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-17102022_change_modlel-1783861900", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```