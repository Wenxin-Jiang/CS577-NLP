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
  emissions: 71.50478540100151
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2331873598
- CO2 Emissions (in grams): 71.5048

## Validation Metrics

- Loss: 1.513
- Rouge1: 49.414
- Rouge2: 24.843
- RougeL: 41.157
- RougeLsum: 44.732
- Gen Len: 18.258

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/dippatel11/autotrain-dippatel_summarizer-2331873598
```