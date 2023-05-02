---
language: 
  - en
tags:
- text generation
- pytorch
- causal-lm
license: apache-2.0
---
# ReGPT-125M-200G
This model was trained on GPT-Neo-125M with [Mengzi Retrieval LM](https://github.com/Langboat/mengzi-retrieval-lm). 

For more details, please refer to this [document](https://github.com/Langboat/mengzi-retrieval-lm/blob/main/README.md).

# How to use
You have to use a forked transformers: https://github.com/Langboat/transformers
```python
from transformers import Re_gptForCausalLM
model = Re_gptForCausalLM.from_pretrained('Langboat/ReGPT-125M-200G')
```
