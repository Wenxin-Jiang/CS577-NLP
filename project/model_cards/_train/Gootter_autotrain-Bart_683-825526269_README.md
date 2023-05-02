---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Gootter/autotrain-data-Bart_683
co2_eq_emissions: 28.12268287254098
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 825526269
- CO2 Emissions (in grams): 28.12268287254098

## Validation Metrics

- Loss: 2.836289644241333
- Rouge1: 31.9867
- Rouge2: 10.3239
- RougeL: 21.0603
- RougeLsum: 30.0862
- Gen Len: 142.0

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Gootter/autotrain-Bart_683-825526269
```