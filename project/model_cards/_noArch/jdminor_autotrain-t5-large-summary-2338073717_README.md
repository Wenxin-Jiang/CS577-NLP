---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- jdminor/autotrain-data-t5-large-summary
co2_eq_emissions:
  emissions: 0.2958140546196442
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2338073717
- CO2 Emissions (in grams): 0.2958

## Validation Metrics

- Loss: 1.536
- Rouge1: 45.911
- Rouge2: 18.396
- RougeL: 36.497
- RougeLsum: 40.822
- Gen Len: 23.070

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/jdminor/autotrain-t5-large-summary-2338073717
```