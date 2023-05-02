---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
co2_eq_emissions:
  emissions: 2295.967887402507
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2346773844
- CO2 Emissions (in grams): 2295.9679

## Validation Metrics

- Loss: 2.208
- Rouge1: 26.910
- Rouge2: 14.562
- RougeL: 24.804
- RougeLsum: 25.155
- Gen Len: 19.930

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Alfred-o/autotrain-tag-href-2346773844
```