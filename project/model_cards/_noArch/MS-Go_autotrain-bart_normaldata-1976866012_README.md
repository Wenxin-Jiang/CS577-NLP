---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- MS-Go/autotrain-data-bart_normaldata
co2_eq_emissions:
  emissions: 41.152874017879256
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1976866012
- CO2 Emissions (in grams): 41.1529

## Validation Metrics

- Loss: 2.837
- Rouge1: 34.318
- Rouge2: 6.495
- RougeL: 18.460
- RougeLsum: 30.998
- Gen Len: 141.027

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/MS-Go/autotrain-bart_normaldata-1976866012
```