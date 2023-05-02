---
language: 
- en
thumbnail: "https://github.com/faGH/fa.creative/blob/master/Icons/FrostAura/FA%20Logo/FrostAura.Logo.Complex.png?raw=true"
tags:
- text-generation
- novel-generation
- fiction
- gpt-neo-x
- pytorch
license: "mit"
---

<p align="center">
  <img src="https://github.com/faGH/fa.creative/blob/master/Icons/FrostAura/FA%20Logo/FrostAura.Logo.Complex.png?raw=true" width="75" title="hover text">
</p>

# fa.intelligence.models.generative.novels.fiction
## Description
This FrostAura Intelligence model is a fine-tuned version of [EleutherAI/gpt-neox-20b](https://huggingface.co/EleutherAI/gpt-neox-20b) for fictional text content generation.

## Getting Started
### PIP Installation
```
pip install -U --no-cache-dir transformers
```
### Usage
```
from transformers import GPTNeoXForCausalLM, GPTNeoXTokenizerFast

model_name = 'FrostAura/gpt-neox-20b-fiction-novel-generation'
model = GPTNeoXForCausalLM.from_pretrained(model_name)
tokenizer = GPTNeoXTokenizerFast.from_pretrained(model_name)

prompt = 'GPTNeoX20B is a 20B-parameter autoregressive Transformer model developed by EleutherAI.'

input_ids = tokenizer(prompt, return_tensors="pt").input_ids

gen_tokens = model.generate(
  input_ids,
  do_sample=True,
  temperature=0.9,
  max_length=100,
)
gen_text = tokenizer.batch_decode(gen_tokens)[0]

print(f'Result: {gen_text}')
```

## Further Fine-Tuning
`in development`

## Support
If you enjoy FrostAura open-source content and would like to support us in continuous delivery, please consider a donation via a platform of your choice.

| Supported Platforms | Link |
| ------------------- | ---- |
| PayPal | [Donate via Paypal](https://www.paypal.com/donate/?hosted_button_id=SVEXJC9HFBJ72) |

For any queries, contact dean.martin@frostaura.net.