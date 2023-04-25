---
tags:
- autotrain
- text-classification
language:
- es
widget:
- text: "El Fútbol Club Barcelona, conocido popularmente como Barça, es una entidad polideportiva con sede en Barcelona, España."
datasets:
- crodri/autotrain-data-wikicat_es
co2_eq_emissions:
  emissions: 10.4216765068249
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2213570987
- CO2 Emissions (in grams): 10.4217

## Validation Metrics

- Loss: 0.713
- Accuracy: 0.786
- Macro F1: 0.758
- Micro F1: 0.786
- Weighted F1: 0.785
- Macro Precision: 0.762
- Micro Precision: 0.786
- Weighted Precision: 0.787
- Macro Recall: 0.757
- Micro Recall: 0.786
- Weighted Recall: 0.786


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/crodri/autotrain-wikicat_es-2213570987
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("crodri/autotrain-wikicat_es-2213570987", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("crodri/autotrain-wikicat_es-2213570987", use_auth_token=True)

inputs = tokenizer("El Fútbol Club Barcelona, conocido popularmente como Barça, es una entidad polideportiva con sede en Barcelona, España.", return_tensors="pt")

outputs = model(**inputs)
```