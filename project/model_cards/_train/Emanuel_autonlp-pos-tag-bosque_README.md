---
tags: autonlp
language: pt
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Emanuel/autonlp-data-pos-tag-bosque
co2_eq_emissions: 6.2107269129101805
---

# Model Trained Using AutoNLP

- Problem type: Entity Extraction
- Model ID: 21124427
- CO2 Emissions (in grams): 6.2107269129101805

## Validation Metrics

- Loss: 0.09813392907381058
- Accuracy: 0.9714309035997062
- Precision: 0.9721275936822545
- Recall: 0.9735345807918949
- F1: 0.9728305785123967

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Emanuel/autonlp-pos-tag-bosque-21124427
```

Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Emanuel/autonlp-pos-tag-bosque")

tokenizer = AutoTokenizer.from_pretrained("Emanuel/autonlp-pos-tag-bosque")

inputs = tokenizer("A noiva casa de branco", return_tensors="pt")

outputs = model(**inputs)

labelids = outputs.logits.squeeze().argmax(axis=-1)
labels = [model.config.id2label[int(x)] for x in labelids]
labels = labels[1:-1]# Filter start and end of sentence symbols

```