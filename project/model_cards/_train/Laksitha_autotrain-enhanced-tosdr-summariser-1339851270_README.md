---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Laksitha/autotrain-data-enhanced-tosdr-summariser
co2_eq_emissions:
  emissions: 0.00773232061494705
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1339851270
- CO2 Emissions (in grams): 0.0077

## Validation Metrics

- Loss: 2.532
- Rouge1: 35.065
- Rouge2: 14.118
- RougeL: 20.884
- RougeLsum: 31.861
- Gen Len: 90.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Laksitha/autotrain-enhanced-tosdr-summariser-1339851270
```