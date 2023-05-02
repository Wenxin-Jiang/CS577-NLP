---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- PoseyATX/autotrain-data-awfulnewdatatrain
co2_eq_emissions:
  emissions: 0.35245501494966197
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2940685240
- CO2 Emissions (in grams): 0.3525

## Validation Metrics

- Loss: 1.182
- Rouge1: 69.284
- Rouge2: 55.274
- RougeL: 61.472
- RougeLsum: 66.749
- Gen Len: 130.111

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/PoseyATX/autotrain-awfulnewdatatrain-2940685240
```