---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Gowtham2003/autotrain-data-autotrain-t5-cnn
co2_eq_emissions:
  emissions: 10.839262225533137
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2662379993
- CO2 Emissions (in grams): 10.8393

## Validation Metrics

- Loss: 1.685
- Rouge1: 23.865
- Rouge2: 10.983
- RougeL: 19.696
- RougeLsum: 22.456
- Gen Len: 18.990

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Gowtham2003/autotrain-autotrain-t5-cnn-2662379993
```