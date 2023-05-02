---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Aman6917/autotrain-data-tm3_model
co2_eq_emissions:
  emissions: 9.38482304577412
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2711480628
- CO2 Emissions (in grams): 9.3848

## Validation Metrics

- Loss: 0.088
- Rouge1: 94.638
- Rouge2: 90.173
- RougeL: 93.188
- RougeLsum: 93.163
- Gen Len: 66.529

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Aman6917/autotrain-tm3_model-2711480628
```