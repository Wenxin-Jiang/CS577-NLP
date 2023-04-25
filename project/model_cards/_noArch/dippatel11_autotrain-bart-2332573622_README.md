---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- dippatel11/autotrain-data-bart
co2_eq_emissions:
  emissions: 17.308721714114615
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2332573622
- CO2 Emissions (in grams): 17.3087

## Validation Metrics

- Loss: 1.460
- Rouge1: 40.163
- Rouge2: 20.060
- RougeL: 30.916
- RougeLsum: 37.538
- Gen Len: 60.370

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/dippatel11/autotrain-bart-2332573622
```