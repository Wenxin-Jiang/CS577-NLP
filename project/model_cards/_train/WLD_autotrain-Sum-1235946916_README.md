---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- WLD/autotrain-data-Sum
co2_eq_emissions:
  emissions: 292.2926477361632
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1235946916
- CO2 Emissions (in grams): 292.2926

## Validation Metrics

- Loss: 2.912
- Rouge1: 23.807
- Rouge2: 10.396
- RougeL: 21.142
- RougeLsum: 21.101
- Gen Len: 13.017

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/WLD/autotrain-Sum-1235946916
```