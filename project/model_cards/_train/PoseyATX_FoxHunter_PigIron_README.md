---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- PoseyATX/autotrain-data-foxhunterirontesting
co2_eq_emissions:
  emissions: 25.447577064303335
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2874884135
- CO2 Emissions (in grams): 25.4476

## Validation Metrics

- Loss: 1.027
- Rouge1: 60.232
- Rouge2: 42.909
- RougeL: 47.915
- RougeLsum: 54.128
- Gen Len: 193.351

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/PoseyATX/autotrain-foxhunterirontesting-2874884135
```