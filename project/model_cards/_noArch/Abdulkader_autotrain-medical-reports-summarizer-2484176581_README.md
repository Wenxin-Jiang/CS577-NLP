---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Abdulkader/autotrain-data-medical-reports-summarizer
co2_eq_emissions:
  emissions: 0.018508154116891218
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2484176581
- CO2 Emissions (in grams): 0.0185

## Validation Metrics

- Loss: 1.728
- Rouge1: 44.555
- Rouge2: 34.430
- RougeL: 44.168
- RougeLsum: 43.895
- Gen Len: 8.930

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Abdulkader/autotrain-medical-reports-summarizer-2484176581
```