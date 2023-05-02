---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- FabsCool/autotrain-data-T5Base1_1
co2_eq_emissions: 583.728921803621
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 728922203
- CO2 Emissions (in grams): 583.728921803621

## Validation Metrics

- Loss: 1.2922444343566895
- Rouge1: 54.3928
- Rouge2: 31.666
- RougeL: 50.3552
- RougeLsum: 50.3694
- Gen Len: 13.3425

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/FabsCool/autotrain-T5Base1_1-728922203
```