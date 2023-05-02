---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
co2_eq_emissions:
  emissions: 2510.751427379945
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2346673849
- CO2 Emissions (in grams): 2510.7514

## Validation Metrics

- Loss: 1.660
- Rouge1: 52.842
- Rouge2: 28.064
- RougeL: 52.252
- RougeLsum: 52.203
- Gen Len: 11.330

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Alfred-o/autotrain-tag-h-2346673849
```