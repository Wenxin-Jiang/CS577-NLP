---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- EricPeter/autonlp-data-MarianMT_lg_en
co2_eq_emissions: 126.34446293851818
---

# Model Trained Using AutoNLP

- Problem type: Machine Translation
- Model ID: 475112539
- CO2 Emissions (in grams): 126.34446293851818

## Validation Metrics

- Loss: 1.5376628637313843
- Rouge1: 62.4613
- Rouge2: 39.4759
- RougeL: 58.183
- RougeLsum: 58.226
- Gen Len: 26.5644

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/EricPeter/autonlp-MarianMT_lg_en-475112539
```