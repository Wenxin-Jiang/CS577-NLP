---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- al02783013/autotrain-data-faseiii_final
co2_eq_emissions:
  emissions: 2.814484312003443
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2312773135
- CO2 Emissions (in grams): 2.8145

## Validation Metrics

- Loss: 0.030
- Accuracy: 0.996
- Precision: 1.000
- Recall: 0.971
- AUC: 0.993
- F1: 0.985

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/al02783013/autotrain-faseiii_final-2312773135
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("al02783013/autotrain-faseiii_final-2312773135", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("al02783013/autotrain-faseiii_final-2312773135", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```