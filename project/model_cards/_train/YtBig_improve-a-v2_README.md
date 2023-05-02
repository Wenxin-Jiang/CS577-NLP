---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
co2_eq_emissions:
  emissions: 1984.9185935944208
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2346173853
- CO2 Emissions (in grams): 1984.9186

## Validation Metrics

- Loss: 0.279
- Rouge1: 63.536
- Rouge2: 40.297
- RougeL: 63.217
- RougeLsum: 63.205
- Gen Len: 13.697

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Alfred-o/autotrain-improve-a-2346173853
```