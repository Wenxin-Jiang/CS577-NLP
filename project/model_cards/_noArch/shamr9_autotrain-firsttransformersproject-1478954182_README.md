---
tags:
- autotrain
- summarization
language:
- ar
widget:
- text: "I love AutoTrain 🤗"
datasets:
- shamr9/autotrain-data-firsttransformersproject
co2_eq_emissions:
  emissions: 5.113476145275885
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1478954182
- CO2 Emissions (in grams): 5.1135

## Validation Metrics

- Loss: 0.534
- Rouge1: 4.247
- Rouge2: 0.522
- RougeL: 4.260
- RougeLsum: 4.241
- Gen Len: 18.928

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/shamr9/autotrain-firsttransformersproject-1478954182
```