---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Kamuuung/autonlp-data-lessons_tagging
co2_eq_emissions: 7.968891750522204
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 606217261
- CO2 Emissions (in grams): 7.968891750522204

## Validation Metrics

- Loss: 0.989620566368103
- Accuracy: 0.6777163904235728
- Macro F1: 0.6817448899563519
- Micro F1: 0.6777163904235728
- Weighted F1: 0.6590820060806175
- Macro Precision: 0.7028251935864661
- Micro Precision: 0.6777163904235728
- Weighted Precision: 0.6764567648776801
- Macro Recall: 0.6861061576846053
- Micro Recall: 0.6777163904235728
- Weighted Recall: 0.6777163904235728


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Kamuuung/autonlp-lessons_tagging-606217261
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Kamuuung/autonlp-lessons_tagging-606217261", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Kamuuung/autonlp-lessons_tagging-606217261", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```