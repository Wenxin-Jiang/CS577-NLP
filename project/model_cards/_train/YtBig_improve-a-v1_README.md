---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
co2_eq_emissions:
  emissions: 0.9899872350262614
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1822063032
- CO2 Emissions (in grams): 0.9900

## Validation Metrics

- Loss: 0.347
- Rouge1: 66.429
- Rouge2: 29.419
- RougeL: 66.188
- RougeLsum: 66.183
- Gen Len: 11.256

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/aalbertini90/autotrain-improve-a-1822063032
```