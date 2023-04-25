---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- jdminor/autotrain-data-pegasus-large-summary-2.0
co2_eq_emissions:
  emissions: 74.34647142824745
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2338573727
- CO2 Emissions (in grams): 74.3465

## Validation Metrics

- Loss: 1.562
- Rouge1: 45.675
- Rouge2: 19.602
- RougeL: 36.750
- RougeLsum: 40.715
- Gen Len: 17.977

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/jdminor/autotrain-pegasus-large-summary-2.0-2338573727
```