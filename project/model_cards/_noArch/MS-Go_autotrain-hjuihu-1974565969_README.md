---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- MS-Go/autotrain-data-hjuihu
co2_eq_emissions:
  emissions: 49.671043265609676
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1974565969
- CO2 Emissions (in grams): 49.6710

## Validation Metrics

- Loss: 2.889
- Rouge1: 36.489
- Rouge2: 7.128
- RougeL: 18.766
- RougeLsum: 33.217
- Gen Len: 141.972

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/MS-Go/autotrain-hjuihu-1974565969
```