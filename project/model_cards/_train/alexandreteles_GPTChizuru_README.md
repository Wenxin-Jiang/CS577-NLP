---
license: cc0-1.0
thumbnail: https://huggingface.co/front/thumbnails/dialogpt.png
tags:
- conversational
datasets:
- alexandreteles/chizuru-ichinose
model-index:
- name: gptchizuru
  results:
  - task:
      type: conversational
      name: Conversational
    dataset:
      type: alexandreteles/chizuru-ichinose
      name: chizuru
    metrics:
      - type: perplexity
        value: 1.0784
        name: Perplexity
        verified: false
---

## Chizuru Ichinose as a DialoGPT model

This model is a fine-tuned version of [DialoGPT-medium](https://huggingface.co/microsoft/DialoGPT-medium/) trained on the [Chizuru Ichinose conversational dataset](https://huggingface.co/datasets/alexandreteles/chizuru-ichinose).

We recommend using one of the Transformers pre-built pipelines to keep context without too much work when running this or any DialoGPT model:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, Conversational

# load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("alexandreteles/GPTChizuru")
model = AutoModelForCausalLM.from_pretrained("alexandreteles/GPTChizuru")

# create pipeline
pipe = pipeline(task="conversational", model=model, tokenizer=tokenizer)

# generate response
print(pipe(Conversation("How are you?")))

```