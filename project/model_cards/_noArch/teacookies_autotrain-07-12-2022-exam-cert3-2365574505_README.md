---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-07-12-2022-exam-cert3
co2_eq_emissions:
  emissions: 26.625950331996258
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 2365574505
- CO2 Emissions (in grams): 26.6260

## Validation Metrics

- Loss: 0.020
- Accuracy: 0.995
- Precision: 0.929
- Recall: 0.945
- F1: 0.937

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-07-12-2022-exam-cert3-2365574505
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-07-12-2022-exam-cert3-2365574505", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-07-12-2022-exam-cert3-2365574505", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```