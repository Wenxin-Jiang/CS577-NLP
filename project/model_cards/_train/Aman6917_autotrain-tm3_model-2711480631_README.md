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
  emissions: 9.180873432477254
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2711480631
- CO2 Emissions (in grams): 9.1809

## Validation Metrics

- Loss: 0.088
- Rouge1: 94.701
- Rouge2: 90.005
- RougeL: 93.006
- RougeLsum: 93.078
- Gen Len: 66.529

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Aman6917/autotrain-tm3_model-2711480631
```