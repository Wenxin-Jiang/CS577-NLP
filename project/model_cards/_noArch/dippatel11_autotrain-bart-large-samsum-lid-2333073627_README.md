---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- dippatel11/autotrain-data-bart-large-samsum-lid
co2_eq_emissions:
  emissions: 4.671853339537159
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2333073627
- CO2 Emissions (in grams): 4.6719

## Validation Metrics

- Loss: 1.499
- Rouge1: 47.617
- Rouge2: 23.262
- RougeL: 39.771
- RougeLsum: 43.344
- Gen Len: 18.088

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/dippatel11/autotrain-bart-large-samsum-lid-2333073627
```