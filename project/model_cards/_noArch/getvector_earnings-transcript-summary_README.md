---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- joshuaperk/autotrain-data-earnings-transcript-summary
co2_eq_emissions:
  emissions: 1.3579793641309694
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1497554606
- CO2 Emissions (in grams): 1.3580

## Validation Metrics

- Loss: 2.246
- Rouge1: 32.105
- Rouge2: 19.375
- RougeL: 26.838
- RougeLsum: 27.080
- Gen Len: 19.417

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/joshuaperk/autotrain-earnings-transcript-summary-1497554606
```