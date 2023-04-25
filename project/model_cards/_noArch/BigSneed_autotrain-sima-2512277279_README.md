---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- BigSneed/autotrain-data-sima
co2_eq_emissions:
  emissions: 1.7528609470694885
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2512277279
- CO2 Emissions (in grams): 1.7529

## Validation Metrics

- Loss: 4.313
- Rouge1: 10.778
- Rouge2: 3.220
- RougeL: 8.286
- RougeLsum: 9.532
- Gen Len: 13.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/BigSneed/autotrain-sima-2512277279
```