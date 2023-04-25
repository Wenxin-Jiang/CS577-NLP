---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Eric Peter/autonlp-data-EN-LUG
co2_eq_emissions: 133.0219882109991
---

# Model Trained Using AutoNLP

- Problem type: Machine Translation
- Model ID: 474612462
- CO2 Emissions (in grams): 133.0219882109991

## Validation Metrics

- Loss: 1.336498737335205
- Rouge1: 52.5404
- Rouge2: 31.6639
- RougeL: 50.1696
- RougeLsum: 50.3398
- Gen Len: 39.046

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/EricPeter/autonlp-EN-LUG-474612462
```