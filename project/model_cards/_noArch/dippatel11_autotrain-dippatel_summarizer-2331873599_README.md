---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- dippatel11/autotrain-data-dippatel_summarizer
co2_eq_emissions:
  emissions: 68.41274041098731
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2331873599
- CO2 Emissions (in grams): 68.4127

## Validation Metrics

- Loss: 1.513
- Rouge1: 49.434
- Rouge2: 24.817
- RougeL: 41.176
- RougeLsum: 44.737
- Gen Len: 18.258

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/dippatel11/autotrain-dippatel_summarizer-2331873599
```