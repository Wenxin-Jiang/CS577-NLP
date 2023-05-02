---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Aman6917/autotrain-data-tm3_model
co2_eq_emissions:
  emissions: 8.016071286117265
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2711480629
- CO2 Emissions (in grams): 8.0161

## Validation Metrics

- Loss: 0.088
- Rouge1: 94.701
- Rouge2: 89.907
- RougeL: 92.992
- RougeLsum: 93.163
- Gen Len: 66.529

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Aman6917/autotrain-tm3_model-2711480629
```