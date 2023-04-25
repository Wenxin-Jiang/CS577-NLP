---
tags:
- transformers
- pytorch
- autotrain
- text-classification
language:
- pt
widget:
- text: I love AutoTrain 🤗
datasets:
- alexandreteles/told_br_binary_sm
co2_eq_emissions:
  emissions: 4.429755329718354
model-index:
- name: told_br_binary_sm
  results:
  - task:
      type: binary-classification
      name: Binary Classification
    dataset:
      type: alexandreteles/told_br_binary_sm
      name: told-br-small
    metrics:
    - type: accuracy
      value: 0.8
      name: Accuracy
      verified: true
    - type: f1
      value: 0.759
      name: F1
      verified: true
    - type: roc_auc
      value: 0.891
      name: AUC
      verified: true
library_name: transformers
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2489276793
- Base model: bert-base-multilingual-cased
- Parameters: 109M
- Model size: 416MB
- CO2 Emissions (in grams): 4.4298

## Validation Metrics

- Loss: 0.432
- Accuracy: 0.800
- Precision: 0.823
- Recall: 0.704
- AUC: 0.891
- F1: 0.759

## Usage

This model was trained on a random subset of the [told-br](https://huggingface.co/datasets/told-br) dataset (1/3 of the original size). Our main objective is to provide a small
model that can be used to classify Brazilian Portuguese tweets in a binary way ('toxic' or 'non toxic').

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/alexandreteles/autotrain-told_br_binary_sm-2489276793
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("alexandreteles/told_br_binary_sm")

tokenizer = AutoTokenizer.from_pretrained("alexandreteles/told_br_binary_sm")

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```