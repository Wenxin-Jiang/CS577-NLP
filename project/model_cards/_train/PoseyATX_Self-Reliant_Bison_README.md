---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- PoseyATX/autotrain-data-letsgettoseventy
co2_eq_emissions:
  emissions: 160.69662192250064
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2941585271
- CO2 Emissions (in grams): 160.6966

## Validation Metrics

- Loss: 0.850
- Rouge1: 65.871
- Rouge2: 50.714
- RougeL: 55.782
- RougeLsum: 60.308
- Gen Len: 127.369

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/PoseyATX/autotrain-letsgettoseventy-2941585271
```