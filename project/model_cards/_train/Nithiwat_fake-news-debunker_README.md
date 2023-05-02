---
tags: autotrain
language: en
widget:
- text: "Bill Gates wants to use mass Covid-19 vaccination campaign to implant microchips to track people"

datasets:
- Fake and real news datasets by CLÉMENT BISAILLON
co2_eq_emissions: 4.415122243239347
---

# Model Trained Using AutoTrain

- Problem: Fake News Classification
- Problem type: Binary Classification
- Model ID: 785124234
- CO2 Emissions (in grams): 4.415122243239347

## Validation Metrics

- Loss: 0.00012586714001372457
- Accuracy: 0.9998886538247411
- Precision: 1.0
- Recall: 0.9997665732959851
- AUC: 0.9999999999999999
- F1: 0.999883273024396

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Nithiwat/autotrain-fake-news-classifier-785124234
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Nithiwat/autotrain-fake-news-classifier-785124234", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Nithiwat/autotrain-fake-news-classifier-785124234", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```