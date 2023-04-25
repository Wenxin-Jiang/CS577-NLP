---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- asadcr/autotrain-data-intelligize-edgar-analysis-2
co2_eq_emissions:
  emissions: 0.9669951284881569
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1722460190
- CO2 Emissions (in grams): 0.9670

## Validation Metrics

- Loss: 1.652
- Rouge1: 50.229
- Rouge2: 41.591
- RougeL: 50.229
- RougeLsum: 53.205
- Gen Len: 10.250

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/asadcr/autotrain-intelligize-edgar-analysis-2-1722460190
```