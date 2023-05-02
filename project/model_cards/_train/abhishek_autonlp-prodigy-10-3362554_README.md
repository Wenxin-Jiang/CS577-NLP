---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- abhishek/autonlp-data-prodigy-10
co2_eq_emissions: 5.340540212393564
---

# Model Trained Using AutoNLP

- Problem type: Entity Extraction
- Model ID: 3362554
- CO2 Emissions (in grams): 5.340540212393564

## Validation Metrics

- Loss: 0.14167872071266174
- Accuracy: 0.9587076867229332
- Precision: 0.7351351351351352
- Recall: 0.7923728813559322
- F1: 0.7626816212082591

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-prodigy-10-3362554
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("abhishek/autonlp-prodigy-10-3362554", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-prodigy-10-3362554", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```