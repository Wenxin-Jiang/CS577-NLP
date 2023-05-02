---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- ScarlettSun9/autotrain-data-ZuoZhuan
co2_eq_emissions: 8.343592303925112
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1100540141
- CO2 Emissions (in grams): 8.343592303925112

## Validation Metrics

- Loss: 0.38094884157180786
- Accuracy: 0.8795777325860159
- Precision: 0.8171375141922127
- Recall: 0.8417033571821684
- F1: 0.8292385373953709

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/ScarlettSun9/autotrain-ZuoZhuan-1100540141
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("ScarlettSun9/autotrain-ZuoZhuan-1100540141", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("ScarlettSun9/autotrain-ZuoZhuan-1100540141", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```