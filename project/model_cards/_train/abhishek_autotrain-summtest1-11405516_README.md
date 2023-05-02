---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- abhishek/autotrain-data-summtest1
co2_eq_emissions: 28.375764585180136
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 11405516
- CO2 Emissions (in grams): 28.375764585180136

## Validation Metrics

- Loss: 1.5257819890975952
- Rouge1: 41.9534
- Rouge2: 18.5044
- RougeL: 34.7507
- RougeLsum: 38.6091
- Gen Len: 15.1037

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/abhishek/autotrain-summtest1-11405516
```