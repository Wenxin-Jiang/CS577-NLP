---
tags: autonlp
language: bn
widget:
- text: "I love AutoNLP 🤗"
datasets:
- albertvillanova/autonlp-data-indic_glue-multi_class_classification-1e67664
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 1311135

## Validation Metrics

- Loss: 0.35616958141326904
- Accuracy: 0.8979447200566973
- Macro F1: 0.8545383956197669
- Micro F1: 0.8979447200566975
- Weighted F1: 0.8983951947775538
- Macro Precision: 0.8615833774439791
- Micro Precision: 0.8979447200566973
- Weighted Precision: 0.9013559365881655
- Macro Recall: 0.8516503001777104
- Micro Recall: 0.8979447200566973
- Weighted Recall: 0.8979447200566973


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/albertvillanova/autonlp-indic_glue-multi_class_classification-1e67664-1311135
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("albertvillanova/autonlp-indic_glue-multi_class_classification-1e67664-1311135", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("albertvillanova/autonlp-indic_glue-multi_class_classification-1e67664-1311135", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```