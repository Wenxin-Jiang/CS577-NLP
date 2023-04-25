---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Laksitha/autotrain-data-tosdr_tldr_legal_summarisation_v1
co2_eq_emissions:
  emissions: 2.9024601099439225
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1434353657
- CO2 Emissions (in grams): 2.9025

## Validation Metrics

- Loss: 2.821
- Rouge1: 32.961
- Rouge2: 10.761
- RougeL: 20.551
- RougeLsum: 30.094
- Gen Len: 92.222

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Laksitha/autotrain-tosdr_tldr_legal_summarisation_v1-1434353657
```