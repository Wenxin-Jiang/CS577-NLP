---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
co2_eq_emissions:
  emissions: 339.29944607016967
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1872663964
- CO2 Emissions (in grams): 339.2994

## Validation Metrics

- Loss: 2.405
- Rouge1: 30.426
- Rouge2: 16.255
- RougeL: 29.262
- RougeLsum: 29.337
- Gen Len: 13.671

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/aalbertini90/autotrain-caption-1872663964
```