---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Aman6917/autotrain-data-fine_tune_table_tm2
co2_eq_emissions:
  emissions: 6.3826736622439215
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2695480537
- CO2 Emissions (in grams): 6.3827

## Validation Metrics

- Loss: 1.227
- Rouge1: 50.065
- Rouge2: 24.621
- RougeL: 46.018
- RougeLsum: 46.230
- Gen Len: 111.647

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Aman6917/autotrain-fine_tune_table_tm2-2695480537
```