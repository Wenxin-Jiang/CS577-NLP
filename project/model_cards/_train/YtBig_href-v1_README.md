---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
co2_eq_emissions:
  emissions: 2.970316260186869
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1900964639
- CO2 Emissions (in grams): 2.9703

## Validation Metrics

- Loss: 2.262
- Rouge1: 27.046
- Rouge2: 14.251
- RougeL: 24.913
- RougeLsum: 25.284
- Gen Len: 19.888

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/aalbertini90/autotrain-href-1900964639
```