---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Neuralearn/autonlp-data-Summarization-AutoNLP
co2_eq_emissions: 155.8470724053265
---

# Model Trained Using AutoNLP

- Problem type: Summarization
- Model ID: 24135330
- CO2 Emissions (in grams): 155.8470724053265

## Validation Metrics

- Loss: 1.369327425956726
- Rouge1: 52.6656
- Rouge2: 30.5879
- RougeL: 40.1268
- RougeLsum: 47.4438
- Gen Len: 75.4625

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/Neuralearn/autonlp-Summarization-AutoNLP-24135330
```