---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- MadhurJindalWorkMail/autonlp-data-Gibb-Detect
co2_eq_emissions: 70.95647633212745
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 515314387
- CO2 Emissions (in grams): 70.95647633212745

## Validation Metrics

- Loss: 0.08077705651521683
- Accuracy: 0.9760103738923709
- Macro F1: 0.9728412857204902
- Micro F1: 0.9760103738923709
- Weighted F1: 0.9759907151741426
- Macro Precision: 0.9736622407675567
- Micro Precision: 0.9760103738923709
- Weighted Precision: 0.97673611876005
- Macro Recall: 0.9728978421381711
- Micro Recall: 0.9760103738923709
- Weighted Recall: 0.9760103738923709


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/MadhurJindalWorkMail/autonlp-Gibb-Detect-515314387
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("MadhurJindalWorkMail/autonlp-Gibb-Detect-515314387", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("MadhurJindalWorkMail/autonlp-Gibb-Detect-515314387", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```