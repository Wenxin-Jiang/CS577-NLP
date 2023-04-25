---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- giuliobrugnaro/autotrain-data-short-description-generator
co2_eq_emissions:
  emissions: 135.05744541394728
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2350573905
- CO2 Emissions (in grams): 135.0574

## Validation Metrics

- Loss: 2.306
- Rouge1: 30.629
- Rouge2: 10.966
- RougeL: 27.506
- RougeLsum: 27.571
- Gen Len: 18.191

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/giuliobrugnaro/autotrain-short-description-generator-2350573905
```