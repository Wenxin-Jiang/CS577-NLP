---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Tarang1998/autonlp-data-pegasus
co2_eq_emissions: 5.680803958729511
---

# Model Trained Using AutoNLP

- Problem type: Summarization
- Model ID: 21664560
- CO2 Emissions (in grams): 5.680803958729511

## Validation Metrics

- Loss: 1.7488420009613037
- Rouge1: 38.1491
- Rouge2: 18.6257
- RougeL: 26.8448
- RougeLsum: 32.2433
- Gen Len: 49.0

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/Tarang1998/autonlp-pegasus-21664560
```