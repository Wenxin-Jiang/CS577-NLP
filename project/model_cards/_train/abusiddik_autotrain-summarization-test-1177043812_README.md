---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- singhajeet13/autotrain-data-summarization-test
co2_eq_emissions: 1166.308824861558
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1177043812
- CO2 Emissions (in grams): 1166.308824861558

## Validation Metrics

- Loss: 1.6226013898849487
- Rouge1: 39.5734
- Rouge2: 18.9817
- RougeL: 33.257
- RougeLsum: 33.2571
- Gen Len: 19.84

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/singhajeet13/autotrain-summarization-test-1177043812
```