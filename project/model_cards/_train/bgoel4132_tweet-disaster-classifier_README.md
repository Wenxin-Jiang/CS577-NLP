---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- bgoel4132/autonlp-data-tweet-disaster-classifier
co2_eq_emissions: 27.22397099134103
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 28716412
- CO2 Emissions (in grams): 27.22397099134103

## Validation Metrics

- Loss: 0.4146720767021179
- Accuracy: 0.8066924731182795
- Macro F1: 0.7835463282531184
- Micro F1: 0.8066924731182795
- Weighted F1: 0.7974252447208724
- Macro Precision: 0.8183917344767431
- Micro Precision: 0.8066924731182795
- Weighted Precision: 0.8005510296861892
- Macro Recall: 0.7679676081852519
- Micro Recall: 0.8066924731182795
- Weighted Recall: 0.8066924731182795


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/bgoel4132/autonlp-tweet-disaster-classifier-28716412
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("bgoel4132/autonlp-tweet-disaster-classifier-28716412", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("bgoel4132/autonlp-tweet-disaster-classifier-28716412", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```