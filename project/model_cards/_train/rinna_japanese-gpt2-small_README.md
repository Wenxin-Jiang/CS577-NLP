---
language: ja
thumbnail: https://github.com/rinnakk/japanese-gpt2/blob/master/rinna.png
tags:
- ja
- japanese
- gpt2
- text-generation
- lm
- nlp
license: mit
datasets:
- cc100
- wikipedia
widget:
- text: "生命、宇宙、そして万物についての究極の疑問の答えは"
---

# japanese-gpt2-small

![rinna-icon](./rinna.png)

This repository provides a small-sized Japanese GPT-2 model. The model was trained using code from Github repository [rinnakk/japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) by [rinna Co., Ltd.](https://corp.rinna.co.jp/)

# How to use the model

~~~~
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt2-small", use_fast=False)
tokenizer.do_lower_case = True  # due to some bug of tokenizer config loading

model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-small")
~~~~

# Model architecture
A 12-layer, 768-hidden-size transformer-based language model.

# Training
The model was trained on [Japanese CC-100](http://data.statmt.org/cc-100/ja.txt.xz) and [Japanese Wikipedia](https://dumps.wikimedia.org/other/cirrussearch) to optimize a traditional language modelling objective on 8\\*V100 GPUs for around 15 days. It reaches around 21 perplexity on a chosen validation set from CC-100.

# Tokenization
The model uses a [sentencepiece](https://github.com/google/sentencepiece)-based tokenizer, the vocabulary was trained on the Japanese Wikipedia using the official sentencepiece training script.

# Licenese
[The MIT license](https://opensource.org/licenses/MIT)
