---
language: 
  - zh
tags:
- text generation
- pytorch
- causal-lm
license: apache-2.0
---

# Mengzi-GPT-neo model (Chinese)
Pretrained model on 300G Chinese corpus. 

## Usage
```python
import torch
import sentencepiece as spm
from transformers import GPTNeoForCausalLM
tokenizer = spm.SentencePieceProcessor(model_file="mengzi_gpt.model")
model = GPTNeoForCausalLM.from_pretrained("Langboat/mengzi-gpt-neo-base")

def lm(prompt, top_k, top_p, max_length, repetition_penalty):
    input_ids = torch.tensor(tokenizer.encode([prompt]), dtype=torch.long, device='cuda')
    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        top_k=top_k,
        top_p=top_p,
        max_length=max_length+len(prompt),
        repetition_penalty=repetition_penalty)
    result = tokenizer.decode(gen_tokens.tolist())[0]
    return result
```
