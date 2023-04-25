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
  emissions: 11.023749088725205
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2392374839
- CO2 Emissions (in grams): 11.0237

## Validation Metrics

- Loss: 0.128
- Rouge1: 94.982
- Rouge2: 91.105
- RougeL: 94.629
- RougeLsum: 94.535
- Gen Len: 30.359

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Aman6917/autotrain-fine_tune_tscholak-2392374839
```