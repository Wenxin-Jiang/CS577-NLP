---
language: 
  - fi
tags:
  - text generation
license: mit
datasets:
- answerable tydiqa
---

# ReadMe

This is a pretrained model based on [Finnish-NLP/gpt2-finnish](https://huggingface.co/Finnish-NLP/gpt2-finnish) that has been trained on [copenlu/answerable_tydiqa](https://huggingface.co/datasets/copenlu/answerable_tydiqa), specifically the text field of the Finnish samples for 2 epochs.

To use the pretrained head, use: `AutoModelForCausalLM.from_pretrained`.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "PartiallyTyped/answerable_tydiqa_lm_pretrained_finnish"
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

```