---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- 0-hero/autotrain-data-legal-summarisation
co2_eq_emissions:
  emissions: 0.14139281336849252
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2269972136
- CO2 Emissions (in grams): 0.1414

## Validation Metrics

- Loss: 2.098
- Rouge1: 36.855
- Rouge2: 22.050
- RougeL: 33.547
- RougeLsum: 34.607
- Gen Len: 27.633

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/0-hero/autotrain-legal-summarisation-2269972136
```