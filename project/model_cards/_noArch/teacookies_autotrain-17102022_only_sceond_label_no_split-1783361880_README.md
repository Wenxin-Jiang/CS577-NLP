---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-17102022_only_sceond_label_no_split
co2_eq_emissions:
  emissions: 18.179473658039548
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1783361880
- CO2 Emissions (in grams): 18.1795

## Validation Metrics

- Loss: 0.013
- Accuracy: 0.997
- Precision: 0.834
- Recall: 0.875
- F1: 0.854

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-17102022_only_sceond_label_no_split-1783361880
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-17102022_only_sceond_label_no_split-1783361880", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-17102022_only_sceond_label_no_split-1783361880", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```