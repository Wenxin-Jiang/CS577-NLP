---
tags: autonlp
language: unk
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Radvian/autonlp-data-indo_summarization
---

# Model Trained Using AutoNLP

- Problem type: Summarization
- Model ID: 14502562

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP", "parameters":{"max_length":1000}}' https://api-inference.huggingface.co/Radvian/autonlp-indo_summarization-14502562
```