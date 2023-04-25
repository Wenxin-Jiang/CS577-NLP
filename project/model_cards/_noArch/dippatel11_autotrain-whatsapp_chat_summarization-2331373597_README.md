---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- dippatel11/autotrain-data-whatsapp_chat_summarization
co2_eq_emissions:
  emissions: 8.016185733770428
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2331373597
- CO2 Emissions (in grams): 8.0162

## Validation Metrics

- Loss: 1.547
- Rouge1: 45.685
- Rouge2: 22.879
- RougeL: 38.559
- RougeLsum: 42.130
- Gen Len: 18.555

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/dippatel11/autotrain-whatsapp_chat_summarization-2331373597
```