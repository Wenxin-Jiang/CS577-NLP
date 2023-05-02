---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
co2_eq_emissions:
  emissions: 4.325625308048844
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2343773834
- CO2 Emissions (in grams): 4.3256

## Validation Metrics

- Loss: 2.080
- Rouge1: 41.882
- Rouge2: 18.838
- RougeL: 39.859
- RougeLsum: 39.919
- Gen Len: 14.611

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Alfred-o/autotrain-title-2343773834
```