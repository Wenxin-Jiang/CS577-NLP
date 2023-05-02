---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Aman6917/autotrain-data-tscholak_finetune_2
co2_eq_emissions:
  emissions: 17.282664720294886
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2548477985
- CO2 Emissions (in grams): 17.2827

## Validation Metrics

- Loss: 0.090
- Rouge1: 96.687
- Rouge2: 93.600
- RougeL: 96.016
- RougeLsum: 96.170
- Gen Len: 32.733

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Aman6917/autotrain-tscholak_finetune_2-2548477985
```