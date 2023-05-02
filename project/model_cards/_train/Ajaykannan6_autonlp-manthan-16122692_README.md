---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Ajaykannan6/autonlp-data-manthan
---

# Model Trained Using AutoNLP

- Problem type: Summarization
- Model ID: 16122692

## Validation Metrics

- Loss: 1.1877621412277222
- Rouge1: 42.0713
- Rouge2: 23.3043
- RougeL: 37.3755
- RougeLsum: 37.8961
- Gen Len: 60.7117

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/Ajaykannan6/autonlp-manthan-16122692
```