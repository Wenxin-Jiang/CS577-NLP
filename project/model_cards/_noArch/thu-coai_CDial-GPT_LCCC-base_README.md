---
license: mit
tags:
- conversational
datasets: silver/lccc
---

## Chinese pre-trained dialogue model (CDial-GPT)

This project provides a large-scale Chinese GPT model pre-trained on the dataset [LCCC](https://huggingface.co/datasets/silver/lccc).

We present a series of Chinese GPT model that are first pre-trained on a Chinese novel dataset and then post-trained on our LCCC dataset.

Similar to [TransferTransfo](https://arxiv.org/abs/1901.08149), we concatenate all dialogue histories into one context sentence, and use this sentence to predict the response. The input of our model consists of word embedding, speaker embedding, and positional embedding of each word.

Paper: [A Large-Scale Chinese Short-Text Conversation Dataset](https://arxiv.org/pdf/2008.03946.pdf)

### How to use

```python
from transformers import OpenAIGPTLMHeadModel, GPT2LMHeadModel, BertTokenizer
import torch
tokenizer = BertTokenizer.from_pretrained("thu-coai/CDial-GPT_LCCC-base")
model = OpenAIGPTLMHeadModel.from_pretrained("thu-coai/CDial-GPT_LCCC-base")
```

For more details, please refer to our [repo.](https://github.com/thu-coai/CDial-GPT) on github.