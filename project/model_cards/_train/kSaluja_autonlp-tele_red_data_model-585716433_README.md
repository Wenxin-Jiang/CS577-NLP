---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- kSaluja/autonlp-data-tele_red_data_model
co2_eq_emissions: 2.379476355147211
---

# Model Trained Using AutoNLP

- Problem type: Entity Extraction
- Model ID: 585716433
- CO2 Emissions (in grams): 2.379476355147211

## Validation Metrics

- Loss: 0.15210922062397003
- Accuracy: 0.9724770642201835
- Precision: 0.950836820083682
- Recall: 0.9625838333921638
- F1: 0.9566742676723382

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/kSaluja/autonlp-tele_red_data_model-585716433
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("kSaluja/autonlp-tele_red_data_model-585716433", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("kSaluja/autonlp-tele_red_data_model-585716433", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```