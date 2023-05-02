---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- PoseyATX/autotrain-data-caribou2billsum
co2_eq_emissions:
  emissions: 611.8280914546775
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2988086239
- CO2 Emissions (in grams): 611.8281

## Validation Metrics

- Loss: 0.199
- Rouge1: 89.446
- Rouge2: 86.014
- RougeL: 87.385
- RougeLsum: 88.542
- Gen Len: 155.343

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/PoseyATX/autotrain-caribou2billsum-2988086239
```