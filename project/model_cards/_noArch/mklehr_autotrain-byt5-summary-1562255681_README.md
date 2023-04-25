---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- mklehr/autotrain-data-byt5-summary
co2_eq_emissions:
  emissions: 2.2525628167913614
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1562255681
- CO2 Emissions (in grams): 2.2526

## Validation Metrics

- Loss: 0.918
- Rouge1: 12.572
- Rouge2: 2.448
- RougeL: 11.701
- RougeLsum: 11.785
- Gen Len: 19.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/mklehr/autotrain-byt5-summary-1562255681
```