---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
co2_eq_emissions:
  emissions: 607.9833800689026
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1822163038
- CO2 Emissions (in grams): 607.9834

## Validation Metrics

- Loss: 1.665
- Rouge1: 53.144
- Rouge2: 27.768
- RougeL: 52.663
- RougeLsum: 52.645
- Gen Len: 10.722

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/aalbertini90/autotrain-h-1822163038
```