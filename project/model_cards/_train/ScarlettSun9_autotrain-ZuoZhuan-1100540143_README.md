---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- ScarlettSun9/autotrain-data-ZuoZhuan
co2_eq_emissions: 14.50120424968173
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1100540143
- CO2 Emissions (in grams): 14.50120424968173

## Validation Metrics

- Loss: 0.3792617619037628
- Accuracy: 0.8799234894798035
- Precision: 0.8133982801130555
- Recall: 0.8416925948973242
- F1: 0.8273035872656656

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/ScarlettSun9/autotrain-ZuoZhuan-1100540143
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("ScarlettSun9/autotrain-ZuoZhuan-1100540143", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("ScarlettSun9/autotrain-ZuoZhuan-1100540143", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```