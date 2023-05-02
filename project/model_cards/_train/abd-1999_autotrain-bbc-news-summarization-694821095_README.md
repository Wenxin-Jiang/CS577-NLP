---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- abd-1999/autotrain-data-bbc-news-summarization
co2_eq_emissions: 2313.4037079026934
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 694821095
- CO2 Emissions (in grams): 2313.4037079026934

## Validation Metrics

- Loss: 3.0294156074523926
- Rouge1: 2.1467
- Rouge2: 0.0853
- RougeL: 2.1524
- RougeLsum: 2.1534
- Gen Len: 18.5603

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/abd-1999/autotrain-bbc-news-summarization-694821095
```