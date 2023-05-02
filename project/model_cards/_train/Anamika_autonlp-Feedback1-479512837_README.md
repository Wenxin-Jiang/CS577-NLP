---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Anamika/autonlp-data-Feedback1
co2_eq_emissions: 123.88023112815048
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 479512837
- CO2 Emissions (in grams): 123.88023112815048

## Validation Metrics

- Loss: 0.6220805048942566
- Accuracy: 0.7961119332705503
- Macro F1: 0.7616345204219084
- Micro F1: 0.7961119332705503
- Weighted F1: 0.795387503907883
- Macro Precision: 0.782839455262034
- Micro Precision: 0.7961119332705503
- Weighted Precision: 0.7992606754484262
- Macro Recall: 0.7451485972167191
- Micro Recall: 0.7961119332705503
- Weighted Recall: 0.7961119332705503


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Anamika/autonlp-Feedback1-479512837
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Anamika/autonlp-Feedback1-479512837", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Anamika/autonlp-Feedback1-479512837", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```