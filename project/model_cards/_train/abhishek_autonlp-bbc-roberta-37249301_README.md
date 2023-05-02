---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- abhishek/autonlp-data-bbc-roberta
co2_eq_emissions: 1.9859980179658823
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 37249301
- CO2 Emissions (in grams): 1.9859980179658823

## Validation Metrics

- Loss: 0.06406362354755402
- Accuracy: 0.9833887043189369
- Macro F1: 0.9832763664701248
- Micro F1: 0.9833887043189369
- Weighted F1: 0.9833288528828136
- Macro Precision: 0.9847257743677181
- Micro Precision: 0.9833887043189369
- Weighted Precision: 0.9835392869652073
- Macro Recall: 0.982101705176067
- Micro Recall: 0.9833887043189369
- Weighted Recall: 0.9833887043189369


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-bbc-roberta-37249301
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-bbc-roberta-37249301", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-bbc-roberta-37249301", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```