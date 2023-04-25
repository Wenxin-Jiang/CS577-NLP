---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- jdminor/autotrain-data-t5-base-samsum
co2_eq_emissions:
  emissions: 49.83285188931273
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2333773650
- CO2 Emissions (in grams): 49.8329

## Validation Metrics

- Loss: 0.987
- Rouge1: 52.508
- Rouge2: 29.367
- RougeL: 44.903
- RougeLsum: 48.446
- Gen Len: 17.123

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/jdminor/autotrain-t5-base-samsum-2333773650
```