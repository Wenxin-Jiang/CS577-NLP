---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Yarn007/autotrain-data-Napkin
co2_eq_emissions: 0.020162211418903533
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 872827783
- CO2 Emissions (in grams): 0.020162211418903533

## Validation Metrics

- Loss: 0.25198695063591003
- Accuracy: 0.9325714285714286
- Macro F1: 0.9254931094274171
- Micro F1: 0.9325714285714286
- Weighted F1: 0.9323540959391766
- Macro Precision: 0.9286720054236212
- Micro Precision: 0.9325714285714286
- Weighted Precision: 0.9324375609546055
- Macro Recall: 0.9227549386201338
- Micro Recall: 0.9325714285714286
- Weighted Recall: 0.9325714285714286


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Yarn007/autotrain-Napkin-872827783
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Yarn007/autotrain-Napkin-872827783", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Yarn007/autotrain-Napkin-872827783", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```