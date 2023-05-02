---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Johny201/autotrain-data-article_pred
co2_eq_emissions: 3.973071565343572
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1142742075
- CO2 Emissions (in grams): 3.973071565343572

## Validation Metrics

- Loss: 0.6098461151123047
- Accuracy: 0.7227722772277227
- Precision: 0.6805555555555556
- Recall: 0.9074074074074074
- AUC: 0.7480299448384554
- F1: 0.7777777777777779

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Johny201/autotrain-article_pred-1142742075
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Johny201/autotrain-article_pred-1142742075", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Johny201/autotrain-article_pred-1142742075", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```