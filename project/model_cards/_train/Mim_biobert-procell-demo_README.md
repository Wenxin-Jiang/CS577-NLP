---
tags: biobert
language: unk
widget:
- text: "Cell lines expressing proteins 🤗"
datasets:
- Mim/autotrain-data-biobert-procell
co2_eq_emissions: 0.5988414315305852
---

# Model Trained Using biobert

- Problem type: Binary Classification
- Model ID: 896229149
- CO2 Emissions (in grams): 0.5988414315305852

## Validation Metrics

- Loss: 0.4045306444168091
- Accuracy: 0.8028169014084507
- Precision: 0.8070175438596491
- Recall: 0.9387755102040817
- AUC: 0.8812615955473099
- F1: 0.8679245283018868

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "Cell lines expressing proteins"}' https://api-inference.huggingface.co/models/Mim/autotrain-biobert-procell-896229149
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Mim/autotrain-biobert-procell-896229149", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Mim/autotrain-biobert-procell-896229149", use_auth_token=True)

inputs = tokenizer("Cell lines expressing proteins", return_tensors="pt")

outputs = model(**inputs)
```