---
tags: autotrain
language: en
widget:
- text: "Why is the username the largest part of each card?"
datasets:
- Shenzy2/autotrain-data-NER4DesignTutor
co2_eq_emissions: 0.004032656988228696
---

# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1169643336
- CO2 Emissions (in grams): 0.004032656988228696

## Validation Metrics

- Loss: 0.677674412727356
- Accuracy: 0.8129095674967235
- Precision: 0.4424778761061947
- Recall: 0.4844961240310077
- F1: 0.4625346901017577

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "Why is the username the largest part of each card?"}' https://api-inference.huggingface.co/models/Shenzy2/NER4DesignTutor
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Shenzy2/NER4DesignTutor")

tokenizer = AutoTokenizer.from_pretrained("Shenzy2/NER4DesignTutor")

inputs = tokenizer("Why is the username the largest part of each card?", return_tensors="pt")

outputs = model(**inputs)
```