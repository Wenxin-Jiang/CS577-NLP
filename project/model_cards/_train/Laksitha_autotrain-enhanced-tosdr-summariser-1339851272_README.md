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
  emissions: 0.011960118277424782
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1339851272
- CO2 Emissions (in grams): 0.0120

## Validation Metrics

- Loss: 2.416
- Rouge1: 34.945
- Rouge2: 12.533
- RougeL: 19.876
- RougeLsum: 31.821
- Gen Len: 92.917

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Laksitha/autotrain-enhanced-tosdr-summariser-1339851272
```