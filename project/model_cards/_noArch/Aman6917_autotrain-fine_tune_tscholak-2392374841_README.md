---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Aman6917/autotrain-data-fine_tune_tscholak
co2_eq_emissions:
  emissions: 11.391305693656719
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2392374841
- CO2 Emissions (in grams): 11.3913

## Validation Metrics

- Loss: 0.138
- Rouge1: 92.363
- Rouge2: 88.743
- RougeL: 92.026
- RougeLsum: 91.574
- Gen Len: 35.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Aman6917/autotrain-fine_tune_tscholak-2392374841
```