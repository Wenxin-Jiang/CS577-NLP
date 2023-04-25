---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-21102022_cert_check_date
co2_eq_emissions:
  emissions: 22.870496971868878
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1828162855
- CO2 Emissions (in grams): 22.8705

## Validation Metrics

- Loss: 0.021
- Accuracy: 0.994
- Precision: 0.867
- Recall: 0.914
- F1: 0.890

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-21102022_cert_check_date-1828162855
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-21102022_cert_check_date-1828162855", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-21102022_cert_check_date-1828162855", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```