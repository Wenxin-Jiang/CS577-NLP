---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Amalq/autotrain-data-smm4h_large_roberta_clean
co2_eq_emissions: 9.123490454955585
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 874027878
- CO2 Emissions (in grams): 9.123490454955585

## Validation Metrics

- Loss: 0.35724225640296936
- Accuracy: 0.8571428571428571
- Precision: 0.7637362637362637
- Recall: 0.8910256410256411
- AUC: 0.9267555361305361
- F1: 0.8224852071005917

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Amalq/autotrain-smm4h_large_roberta_clean-874027878
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Amalq/autotrain-smm4h_large_roberta_clean-874027878", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Amalq/autotrain-smm4h_large_roberta_clean-874027878", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```