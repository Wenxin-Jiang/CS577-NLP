---
language: 
- en
thumbnail: "https://github.com/faGH/fa.creative/blob/master/Icons/FrostAura/FA%20Logo/FrostAura.Logo.Complex.png?raw=true"
tags:
- text-generation
- novel-generation
- fiction
- gpt-neo
- pytorch
license: "mit"
---

<p align="center">
  <img src="https://github.com/faGH/fa.creative/blob/master/Icons/FrostAura/FA%20Logo/FrostAura.Logo.Complex.png?raw=true" width="75" title="hover text">
</p>

# fa.intelligence.models.generative.novels.fiction
## Description
This FrostAura Intelligence model is a fine-tuned version of [EleutherAI/gpt-neo-1.3B](https://huggingface.co/EleutherAI/gpt-neo-1.3B) for fictional text content generation.

## Getting Started
### PIP Installation
```
pip install -U --no-cache-dir transformers
```
### Usage
```
from transformers import pipeline

model_name: str = 'FrostAura/gpt-neo-1.3B-fiction-novel-generation'
generator: pipeline = pipeline('text-generation', model=model_name)

prompt: str = 'So far my day has been '
gen_text: str = generator(prompt, do_sample=True, min_length=50)

print(f'Result: {gen_text}')
```

## Further Fine-Tuning
[in development](https://github.com/dredwardhyde/gpt-neo-fine-tuning-example/blob/main/gpt_neo.py)

## Support
If you enjoy FrostAura open-source content and would like to support us in continuous delivery, please consider a donation via a platform of your choice.

| Supported Platforms | Link |
| ------------------- | ---- |
| PayPal | [Donate via Paypal](https://www.paypal.com/donate/?hosted_button_id=SVEXJC9HFBJ72) |

For any queries, contact dean.martin@frostaura.net.