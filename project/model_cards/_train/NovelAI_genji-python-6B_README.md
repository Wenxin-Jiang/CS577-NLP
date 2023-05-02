---
language:
- en
tags:
- pytorch
- causal-lm
license: apache-2.0
datasets:
- the Pile
---

# Genji-python 6B

For example usage or to easily use the model you can check our colab notebook:
[Notebook](https://colab.research.google.com/drive/1PnWpx02IEUkY8jhLKd_NewUGEXahAska?usp=sharing)

## Model Description

Genji is a transformer model finetuned on EleutherAI's GPT-J 6B model. This particular model is trained on python only code approaching 4GB in size.

| Hyperparameter    | Value  | 
|-------------------|--------|
| n_parameters      | 6,053,381,344 |
| n_layers          | 28*    |
| d_model           | 4,096  |
| d_ff              | 16,384 |
| n_heads           | 16     |
| d_head            | 256    |
| n_ctx             | 2,048  |
| n_vocab           | 50,400 (same tokenizer as GPT-2/3)  |
| position encoding | [Rotary position encodings (RoPE)](https://arxiv.org/abs/2104.09864) |
| RoPE dimensions   | [64](https://github.com/kingoflolz/mesh-transformer-jax/blob/f2aa66e0925de6593dcbb70e72399b97b4130482/mesh_transformer/layers.py#L223) |

`*` each layer consists of one feedforward block and one self attention block

The model consists of 28 layers with a model dimension of 4096, and a feedforward dimension of 16384. The model
dimension is split into 16 heads, each with a dimension of 256. Rotary position encodings (RoPE) was applied to 64
dimensions of each head. The model is trained with a tokenization vocabulary of 50257, using the same set of BPEs as
GPT-2/GPT-3.

## Training data

GPT-J 6B was pretrained on the [Pile](pile.eleuther.ai), a large scale curated dataset created by EleutherAI for the purpose of training this model. After the pre-training, it's finetuned on the python code that was taken from the Pile.

## Training procedure

Genji-python-6B is trained for 20k steps on around 655 million tokens with learning rate of 2e-06

## Intended Use

This model is trained for assistence on writing python code and having fun trying weird stuff with it. 

### How to use

This model is only usable with our fork because GPT-J is not merged to the main transformers repo yet. When it's merged, we will make this model easily loadable.
For now, you need to use this fork:
[Fork](https://github.com/finetuneanon/transformers)

to install with pip:
```bash
pip install git+https://github.com/finetuneanon/transformers@gpt-neo-localattention3-rp-b
```

This model takes more than 16 gigs of RAM to load. If you want more efficient and faster loading, please check our split model.
We recommend the usage of the model as FP16. That way, it fits in 16GB VRAM cards.

How to use:
```python
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    GPTNeoForCausalLM,
)

model = AutoModelForCausalLM.from_pretrained("NovelAI/genji-python-6B", use_auth_token=True).half().eval().cuda()
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")

text = '''def print_customer_name'''

tokens = tokenizer(text, return_tensors="pt").input_ids
generated_tokens = model.generate(tokens.long().cuda(), use_cache=True, do_sample=True, top_k=50, temperature=0.3, top_p=0.9, repetition_penalty=1.125, min_length=1, max_length=len(tokens[0]) + 400, pad_token_id=tokenizer.eos_token_id)
last_tokens = generated_tokens[0][len(tokens[0]):]
generated_text = tokenizer.decode(last_tokens)
print("Generation:\n" + generated_text)
```
When ran, this code generates:
```python
Prompt:
def print_customer_name
Generation:
(self, customer):
        """Print the name of a customer."""
        if not self.is_valid():
            return

        print("Customer: {}".format(customer))
```

For example usage, you can see our colab notebook as well:
[Notebook](https://colab.research.google.com/drive/1PnWpx02IEUkY8jhLKd_NewUGEXahAska?usp=sharing)

## Eval results

TBD

## Acknowledgements

This project was possible because of the compute provided by the
[TPU Research Cloud](https://sites.research.google/trc/)

and [EleutherAI](https://eleuther.ai/) for pretraining of the GPT-J 6B.

Thanks to everyone who contributed to this project!

- [Aero](https://github.com/AeroScripts)
- [Finetune](https://github.com/finetuneanon)
- [Kurumuz](https://github.com/kurumuz)