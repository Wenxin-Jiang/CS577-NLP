---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- rolosaCBTech/autotrain-data-mt5_xlsum_msamsum
co2_eq_emissions:
  emissions: 52.2418341683463
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2231571360
- CO2 Emissions (in grams): 52.2418

## Validation Metrics

- Loss: 1.589
- Rouge1: 43.587
- Rouge2: 22.929
- RougeL: 38.320
- RougeLsum: 38.089
- Gen Len: 23.965

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/rolosaCBTech/autotrain-mt5_xlsum_msamsum-2231571360
```