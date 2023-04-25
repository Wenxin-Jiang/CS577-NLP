---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- abhishekgupta/autotrain-data-question-generation4
co2_eq_emissions:
  emissions: 4.8068340904981115
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2116768409
- CO2 Emissions (in grams): 4.8068

## Validation Metrics

- Loss: 1.092
- Rouge1: 32.336
- Rouge2: 15.558
- RougeL: 30.175
- RougeLsum: 30.191
- Gen Len: 14.493

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/abhishekgupta/autotrain-question-generation4-2116768409
```