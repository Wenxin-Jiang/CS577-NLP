---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
co2_eq_emissions:
  emissions: 2.4435817864698777
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1902664733
- CO2 Emissions (in grams): 2.4436

## Validation Metrics

- Loss: 0.282
- Rouge1: 63.261
- Rouge2: 29.581
- RougeL: 63.239
- RougeLsum: 63.219
- Gen Len: 9.777

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/aalbertini90/autotrain-improve-figcaption-v2-1902664733
```