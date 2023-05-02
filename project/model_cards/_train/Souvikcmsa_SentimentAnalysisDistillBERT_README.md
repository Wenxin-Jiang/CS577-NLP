---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Souvikcmsa/autotrain-data-sentiment_analysis
co2_eq_emissions: 0.015536746909294205
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 762923432
- CO2 Emissions (in grams): 0.015536746909294205

## Validation Metrics

- Loss: 0.49825894832611084
- Accuracy: 0.7962895598399418
- Macro F1: 0.7997458031044901
- Micro F1: 0.7962895598399418
- Weighted F1: 0.796365325858282
- Macro Precision: 0.7995724418486833
- Micro Precision: 0.7962895598399418
- Weighted Precision: 0.7965384250324863
- Macro Recall: 0.8000290112564951
- Micro Recall: 0.7962895598399418
- Weighted Recall: 0.7962895598399418


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Souvikcmsa/autotrain-sentiment_analysis-762923432
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Souvikcmsa/autotrain-sentiment_analysis-762923432", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Souvikcmsa/autotrain-sentiment_analysis-762923432", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```