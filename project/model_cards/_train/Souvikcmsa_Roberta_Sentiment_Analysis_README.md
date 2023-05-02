---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Souvikcmsa/autotrain-data-sentimentAnalysis_By_Souvik
co2_eq_emissions: 4.453029772491864
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 762623422
- CO2 Emissions (in grams): 4.453029772491864

## Validation Metrics

- Loss: 0.40843138098716736
- Accuracy: 0.8302828618968386
- Macro F1: 0.8302447939743022
- Micro F1: 0.8302828618968385
- Weighted F1: 0.8302151855901072
- Macro Precision: 0.8310980209442669
- Micro Precision: 0.8302828618968386
- Weighted Precision: 0.8313262654775467
- Macro Recall: 0.8305699539252172
- Micro Recall: 0.8302828618968386
- Weighted Recall: 0.8302828618968386


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Souvikcmsa/autotrain-sentimentAnalysis_By_Souvik-762623422
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Souvikcmsa/autotrain-sentimentAnalysis_By_Souvik-762623422", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Souvikcmsa/autotrain-sentimentAnalysis_By_Souvik-762623422", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```