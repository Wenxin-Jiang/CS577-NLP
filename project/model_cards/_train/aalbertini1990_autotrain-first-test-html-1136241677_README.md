---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- aalbertini1990/autotrain-data-first-test-html
co2_eq_emissions: 19.49742293318862
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1136241677
- CO2 Emissions (in grams): 19.49742293318862

## Validation Metrics

- Loss: 0.18860992789268494
- Rouge1: 84.2283
- Rouge2: 80.2825
- RougeL: 83.9066
- RougeLsum: 83.9129
- Gen Len: 58.3175

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/aalbertini1990/autotrain-first-test-html-1136241677
```