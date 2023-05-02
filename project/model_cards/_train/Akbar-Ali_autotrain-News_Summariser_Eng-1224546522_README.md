---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Akbar-Ali/autotrain-data-News_Summariser_Eng
co2_eq_emissions:
  emissions: 35.7814981860994
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1224546522
- CO2 Emissions (in grams): 35.7815

## Validation Metrics

- Loss: 0.638
- Rouge1: 44.532
- Rouge2: 33.731
- RougeL: 40.372
- RougeLsum: 40.653
- Gen Len: 57.730

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Akbar-Ali/autotrain-News_Summariser_Eng-1224546522
```