---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
co2_eq_emissions:
  emissions: 5.33165635098582
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2343573836
- CO2 Emissions (in grams): 5.3317

## Validation Metrics

- Loss: 2.315
- Rouge1: 39.655
- Rouge2: 17.178
- RougeL: 38.522
- RougeLsum: 38.554
- Gen Len: 12.059

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Alfred-o/autotrain-tag-figcaption-2343573836
```