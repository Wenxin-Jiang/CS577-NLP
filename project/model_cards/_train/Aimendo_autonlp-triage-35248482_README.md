---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Aimendo/autonlp-data-triage
co2_eq_emissions: 7.989144645413398
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 35248482
- CO2 Emissions (in grams): 7.989144645413398

## Validation Metrics

- Loss: 0.13783401250839233
- Accuracy: 0.9728654124457308
- Macro F1: 0.949537871674076
- Micro F1: 0.9728654124457308
- Weighted F1: 0.9732422812610365
- Macro Precision: 0.9380372699332605
- Micro Precision: 0.9728654124457308
- Weighted Precision: 0.974548513256663
- Macro Recall: 0.9689346153591594
- Micro Recall: 0.9728654124457308
- Weighted Recall: 0.9728654124457308


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Aimendo/autonlp-triage-35248482
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Aimendo/autonlp-triage-35248482", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Aimendo/autonlp-triage-35248482", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```