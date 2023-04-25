---
tags:
- autotrain
widget:
- text: what is a laptop?
datasets:
- breadlicker45/autotrain-data-yahoo-answer-small
co2_eq_emissions:
  emissions: 1.56957741717827
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2422175450
- CO2 Emissions (in grams): 1.5696

## Validation Metrics

- Loss: 3.470
- Rouge1: 11.323
- Rouge2: 2.075
- RougeL: 9.397
- RougeLsum: 10.236
- Gen Len: 16.882

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/breadlicker45/autotrain-yahoo-answer-small-2422175450
```