---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- CH0KUN/autotrain-data-TNC_Domain_WangchanBERTa
co2_eq_emissions: 25.144394918865913
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 921730254
- CO2 Emissions (in grams): 25.144394918865913

## Validation Metrics

- Loss: 0.7080970406532288
- Accuracy: 0.7775925925925926
- Macro F1: 0.7758012615987406
- Micro F1: 0.7775925925925925
- Weighted F1: 0.7758012615987406
- Macro Precision: 0.7833307663368776
- Micro Precision: 0.7775925925925926
- Weighted Precision: 0.7833307663368777
- Macro Recall: 0.7775925925925926
- Micro Recall: 0.7775925925925926
- Weighted Recall: 0.7775925925925926


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/CH0KUN/autotrain-TNC_Domain_WangchanBERTa-921730254
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("CH0KUN/autotrain-TNC_Domain_WangchanBERTa-921730254", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("CH0KUN/autotrain-TNC_Domain_WangchanBERTa-921730254", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```