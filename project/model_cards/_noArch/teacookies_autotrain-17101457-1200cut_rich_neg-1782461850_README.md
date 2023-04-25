---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- teacookies/autotrain-data-17101457-1200cut_rich_neg
co2_eq_emissions:
  emissions: 15.90515729014607
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1782461850
- CO2 Emissions (in grams): 15.9052

## Validation Metrics

- Loss: 0.022
- Accuracy: 0.994
- Precision: 0.736
- Recall: 0.804
- F1: 0.769

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/teacookies/autotrain-17101457-1200cut_rich_neg-1782461850
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("teacookies/autotrain-17101457-1200cut_rich_neg-1782461850", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("teacookies/autotrain-17101457-1200cut_rich_neg-1782461850", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```