---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
co2_eq_emissions:
  emissions: 4721.333535315218
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1670059180
- CO2 Emissions (in grams): 4721.3335

## Validation Metrics

- Loss: 0.201
- Rouge1: 78.850
- Rouge2: 73.326
- RougeL: 78.683
- RougeLsum: 78.683
- Gen Len: 17.217

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' 
```