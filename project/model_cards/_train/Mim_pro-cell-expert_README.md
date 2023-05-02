---
tags: autotrain
language: unk
widget:
- text: "ACE2 overexpression in AAV cell lines"
datasets:
- Mim/autotrain-data-procell-expert
co2_eq_emissions: 0.004814823138367317
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 800724769
- CO2 Emissions (in grams): 0.004814823138367317

## Validation Metrics

- Loss: 0.4749071002006531
- Accuracy: 0.9
- Precision: 0.8928571428571429
- Recall: 0.9615384615384616
- AUC: 0.9065934065934066
- F1: 0.9259259259259259

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Mim/autotrain-procell-expert-800724769
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Mim/autotrain-procell-expert-800724769", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Mim/autotrain-procell-expert-800724769", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```