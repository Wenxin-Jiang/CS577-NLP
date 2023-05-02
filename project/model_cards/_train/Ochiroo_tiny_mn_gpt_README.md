---
language: mn 
---

# GPT2-Mongolia

## Model description

GPT-2 is a transformers model pretrained on a very small corpus of Mongolian news data in a self-supervised fashion. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely, it was trained to guess the next word in sentences.

## How to use

```python
import tensorflow as tf 
from transformers import GPT2Config, TFGPT2LMHeadModel, GPT2Tokenizer
from transformers import WEIGHTS_NAME, CONFIG_NAME

tokenizer = GPT2Tokenizer.from_pretrained('Ochiroo/tiny_mn_gpt')
model = TFGPT2LMHeadModel.from_pretrained('Ochiroo/tiny_mn_gpt')

text = "Намайг Эрдэнэ-Очир гэдэг. Би"

input_ids = tokenizer.encode(text, return_tensors='tf')

beam_outputs = model.generate(
    input_ids,
    max_length = 25,
    num_beams = 5,
    temperature = 0.7,
    no_repeat_ngram_size=2,
    num_return_sequences=5
)
print(tokenizer.decode(beam_outputs[0]))
```

## Training data and biases

Trained on 500MB of Mongolian news dataset (IKON) on RTX 2060. 