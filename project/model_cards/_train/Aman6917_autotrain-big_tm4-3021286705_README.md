---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Aman6917/autotrain-data-big_tm4
co2_eq_emissions:
  emissions: 14.606662709582208
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 3021286705
- CO2 Emissions (in grams): 14.6067

## Validation Metrics

- Loss: 0.000
- Rouge1: 100.000
- Rouge2: 100.000
- RougeL: 100.000
- RougeLsum: 100.000
- Gen Len: 110.556

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Aman6917/autotrain-big_tm4-3021286705
```