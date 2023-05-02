---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Anamika/autonlp-data-fa
co2_eq_emissions: 25.128735714898614
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 473312409
- CO2 Emissions (in grams): 25.128735714898614

## Validation Metrics

- Loss: 0.6010786890983582
- Accuracy: 0.7990650945370823
- Macro F1: 0.7429662929144928
- Micro F1: 0.7990650945370823
- Weighted F1: 0.7977660363770382
- Macro Precision: 0.7744390888231261
- Micro Precision: 0.7990650945370823
- Weighted Precision: 0.800444194278352
- Macro Recall: 0.7198278524814119
- Micro Recall: 0.7990650945370823
- Weighted Recall: 0.7990650945370823


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Anamika/autonlp-fa-473312409
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Anamika/autonlp-fa-473312409", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Anamika/autonlp-fa-473312409", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```