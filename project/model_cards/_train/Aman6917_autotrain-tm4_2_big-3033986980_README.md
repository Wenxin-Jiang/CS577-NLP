---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Aman6917/autotrain-data-tm4_2_big
co2_eq_emissions:
  emissions: 14.618973710629989
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 3033986980
- CO2 Emissions (in grams): 14.6190

## Validation Metrics

- Loss: 0.000
- Rouge1: 100.000
- Rouge2: 100.000
- RougeL: 100.000
- RougeLsum: 100.000
- Gen Len: 110.456

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Aman6917/autotrain-tm4_2_big-3033986980
```