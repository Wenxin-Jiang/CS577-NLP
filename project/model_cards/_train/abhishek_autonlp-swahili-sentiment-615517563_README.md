---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- abhishek/autonlp-data-swahili-sentiment
co2_eq_emissions: 1.9057858628956459
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 615517563
- CO2 Emissions (in grams): 1.9057858628956459

## Validation Metrics

- Loss: 0.6990908980369568
- Accuracy: 0.695364238410596
- Macro F1: 0.6088819062581828
- Micro F1: 0.695364238410596
- Weighted F1: 0.677326207350606
- Macro Precision: 0.6945099492363175
- Micro Precision: 0.695364238410596
- Weighted Precision: 0.6938596845881614
- Macro Recall: 0.5738408020723632
- Micro Recall: 0.695364238410596
- Weighted Recall: 0.695364238410596


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-swahili-sentiment-615517563
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-swahili-sentiment-615517563", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-swahili-sentiment-615517563", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```