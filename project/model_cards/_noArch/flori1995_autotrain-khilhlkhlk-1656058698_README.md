---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- flori1995/autotrain-data-khilhlkhlk
co2_eq_emissions:
  emissions: 0.029594843713370476
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1656058698
- CO2 Emissions (in grams): 0.0296

## Validation Metrics

- Loss: 1.334
- Rouge1: 64.877
- Rouge2: 50.407
- RougeL: 64.527
- RougeLsum: 64.661
- Gen Len: 9.992

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/flori1995/autotrain-khilhlkhlk-1656058698
```