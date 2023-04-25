---
inference: true
tags:
- pytorch
- transformers
- autotrain
- text-classification
language:
- pt
widget:
- text: I love AutoTrain 🤗
datasets:
- alexandreteles/told_br_binary_sm
co2_eq_emissions:
  emissions: 1.778776476039011
model-index:
- name: told_br_binary_sm_bertimbau
  results:
  - task:
      type: binary-classification
      name: Binary Classification
    dataset:
      type: alexandreteles/told_br_binary_sm
      name: told-br
    metrics:
    - type: accuracy
      value: 0.815
      name: Accuracy
      verified: true
    - type: f1
      value: 0.793
      name: F1
      verified: true
    - type: roc_auc
      value: 0.895
      name: AUC
      verified: true
library_name: transformers
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2489776826
- Base model: bert-base-portuguese-cased
- Parameters: 109M
- Model size: 416MB
- CO2 Emissions (in grams): 1.7788

## Validation Metrics

- Loss: 0.412
- Accuracy: 0.815
- Precision: 0.793
- Recall: 0.794
- AUC: 0.895
- F1: 0.793

## Usage

This model was trained on a random subset of the [told-br](https://huggingface.co/datasets/told-br) dataset (1/3 of the original size). Our main objective is to provide a small
model that can be used to classify Brazilian Portuguese tweets in a binary way ('toxic' or 'non toxic').

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/alexandreteles/autotrain-told_br_binary_sm_bertimbau-2489776826
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("alexandreteles/autotrain-told_br_binary_sm_bertimbau-2489776826", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("alexandreteles/autotrain-told_br_binary_sm_bertimbau-2489776826", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```