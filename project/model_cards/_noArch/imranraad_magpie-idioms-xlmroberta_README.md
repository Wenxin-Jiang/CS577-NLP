---
tags:
- autotrain
- token-classification
language:
- unk
widget:
- text: "I’m sorry but I just can’t seem to wrap my head around it. - I’m sorry but I just can’t seem to understand."
- text: "Why are you so bent out of shape? - Why are you so upset?"
- text: "Listen, it is easier said than done, many people lack commitment."
datasets:
- imranraad/autotrain-data-magpie-metaphor-xlmr
co2_eq_emissions:
  emissions: 9.232131148683266
---

# Fine-tune datasets
 - MAGPIE corpus: https://aclanthology.org/2020.lrec-1.35/

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1590556166
- CO2 Emissions (in grams): 9.2321

## Validation Metrics

- Loss: 0.137
- Accuracy: 0.985
- Precision: 0.000
- Recall: 0.000
- F1: 0.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/imranraad/autotrain-magpie-metaphor-xlmr-1590556166
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("imranraad/autotrain-magpie-metaphor-xlmr-1590556166", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("imranraad/autotrain-magpie-metaphor-xlmr-1590556166", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```