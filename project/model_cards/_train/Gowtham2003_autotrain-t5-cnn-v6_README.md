---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Gowtham2003/autotrain-data-autotrain-t5-cnn-v6
co2_eq_emissions:
  emissions: 6.1132277010358
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2646779711
- CO2 Emissions (in grams): 6.1132

## Validation Metrics

- Loss: 1.798
- Rouge1: 23.476
- Rouge2: 10.592
- RougeL: 19.266
- RougeLsum: 22.050
- Gen Len: 18.988

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Gowtham2003/autotrain-autotrain-t5-cnn-v6-2646779711
```