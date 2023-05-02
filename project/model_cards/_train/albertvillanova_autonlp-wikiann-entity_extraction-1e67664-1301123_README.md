---
tags: autonlp
language: bn
widget:
- text: "I love AutoNLP 🤗"
datasets:
- albertvillanova/autonlp-data-wikiann-entity_extraction-1e67664
---

# Model Trained Using AutoNLP

- Problem type: Entity Extraction
- Model ID: 1301123

## Validation Metrics

- Loss: 0.14097803831100464
- Accuracy: 0.9740097463451206
- Precision: 0.0
- Recall: 0.0
- F1: 0.0

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/albertvillanova/autonlp-wikiann-entity_extraction-1e67664-1301123
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("albertvillanova/autonlp-wikiann-entity_extraction-1e67664-1301123", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("albertvillanova/autonlp-wikiann-entity_extraction-1e67664-1301123", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```