---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Hodiden/autotrain-data-TestProj
co2_eq_emissions: 8.052949236815056
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 722121991
- CO2 Emissions (in grams): 8.052949236815056

## Validation Metrics

- Loss: 1.123626708984375
- Rouge1: 56.1275
- Rouge2: 33.5648
- RougeL: 51.986
- RougeLsum: 51.9943
- Gen Len: 13.2823

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Hodiden/autotrain-TestProj-722121991
```