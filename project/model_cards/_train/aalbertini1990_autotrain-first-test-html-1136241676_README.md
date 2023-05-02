---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- aalbertini1990/autotrain-data-first-test-html
co2_eq_emissions: 684.7105644305452
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1136241676
- CO2 Emissions (in grams): 684.7105644305452

## Validation Metrics

- Loss: 0.2270897775888443
- Rouge1: 63.4452
- Rouge2: 60.0038
- RougeL: 63.3343
- RougeLsum: 63.321
- Gen Len: 19.1562

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/aalbertini1990/autotrain-first-test-html-1136241676
```