---
tags:
- generated_from_keras_callback
model-index:
- name: tmpq0jhm_jh
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

## Model description

This is a gpt2 model trained on 142 612 different Lithuanian Wikipedia articles + 11 405 articles taken from delfi.lt, ve.lt and respublika.lt news portals.

## Intended uses & limitations

This is a model I trained when writing my bachelors. You can use it anywhere you want.

### Training results

Model reached 36.83% accuracy with training data and 37.02% with validation data

### Framework versions

 Transformers 3.5.0
 TensorFlow 2.4.1
 Tokenizers 0.12.1
 Torch 1.4.0

How to use it:

```python
import tensorflow as tf
from transformers import WEIGHTS_NAME, CONFIG_NAME
from transformers import GPT2Config, TFGPT2LMHeadModel, GPT2Tokenizer
import os
output_dir = '...' #local file or link to this page
tokenizer = GPT2Tokenizer.from_pretrained(output_dir)
model = TFGPT2LMHeadModel.from_pretrained(output_dir)

text = "Siekdamas"
# encoding the input text
input_ids = tokenizer.encode(text, return_tensors='tf')
# getting out output
beam_outputs = model.generate(
  input_ids,
  max_length = 150,
  num_beams = 5,
  temperature = 0.7,
  no_repeat_ngram_size=2,
  num_return_sequences=5
)

print(tokenizer.decode(beam_outputs[0]))
```