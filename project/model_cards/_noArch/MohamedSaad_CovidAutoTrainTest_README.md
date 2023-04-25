---
tags:
- autotrain
- text-classification
language:
- ar
widget:
- text: "I love AutoTrain 🤗"
datasets:
- MohamedSaad/autotrain-data-covid
co2_eq_emissions:
  emissions: 1.7646991170797304
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2509577239
- CO2 Emissions (in grams): 1.7647

## Validation Metrics

- Loss: 1.861
- Accuracy: 0.319
- Macro F1: 0.231
- Micro F1: 0.319
- Weighted F1: 0.337
- Macro Precision: 0.270
- Micro Precision: 0.319
- Weighted Precision: 0.613
- Macro Recall: 0.346
- Micro Recall: 0.319
- Weighted Recall: 0.319


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/MohamedSaad/autotrain-covid-2509577239
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("MohamedSaad/autotrain-covid-2509577239", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("MohamedSaad/autotrain-covid-2509577239", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```