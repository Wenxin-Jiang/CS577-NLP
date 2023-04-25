---
language: ja
thumbnail: https://github.com/rinnakk/japanese-gpt2/blob/master/rinna.png
tags:
- ja
- japanese
- roberta
- masked-lm
- nlp
license: mit
datasets:
- cc100
- wikipedia
mask_token: "[MASK]"
widget:
- text: "[CLS]4年に1度[MASK]は開かれる。"
---

# japanese-roberta-base

![rinna-icon](./rinna.png)

This repository provides a base-sized Japanese RoBERTa model. The model was trained using code from Github repository [rinnakk/japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) by [rinna Co., Ltd.](https://corp.rinna.co.jp/)

# How to load the model

~~~~
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-roberta-base", use_fast=False)
tokenizer.do_lower_case = True  # due to some bug of tokenizer config loading

model = AutoModelForMaskedLM.from_pretrained("rinna/japanese-roberta-base")
~~~~

# How to use the model for masked token prediction

## Note 1: Use `[CLS]`

To predict a masked token, be sure to add a `[CLS]` token before the sentence for the model to correctly encode it, as it is used during the model training.

## Note 2: Use `[MASK]` after tokenization

A) Directly typing `[MASK]` in an input string and B) replacing a token with `[MASK]` after tokenization will yield different token sequences, and thus different prediction results. It is more appropriate to use `[MASK]` after tokenization (as it is consistent with how the model was pretrained). However, the Huggingface Inference API only supports typing `[MASK]` in the input string and produces less robust predictions.

## Note 3: Provide `position_ids` as an argument explicitly

When `position_ids` are not provided for a `Roberta*` model, Huggingface's `transformers` will automatically construct it but start from `padding_idx` instead of `0` (see [issue](https://github.com/rinnakk/japanese-pretrained-models/issues/3) and function `create_position_ids_from_input_ids()` in Huggingface's [implementation](https://github.com/huggingface/transformers/blob/master/src/transformers/models/roberta/modeling_roberta.py)), which unfortunately does not work as expected with `rinna/japanese-roberta-base` since the `padding_idx` of the corresponding tokenizer is not `0`. So please be sure to constrcut the `position_ids` by yourself and make it start from position id `0`.

## Example

Here is an example by to illustrate how our model works as a masked language model. Notice the difference between running the following code example and running the Huggingface Inference API. 

~~~~
# original text
text = "4年に1度オリンピックは開かれる。"

# prepend [CLS]
text = "[CLS]" + text

# tokenize
tokens = tokenizer.tokenize(text)
print(tokens)  # output: ['[CLS]', '▁4', '年に', '1', '度', 'オリンピック', 'は', '開かれる', '。']

# mask a token
masked_idx = 5
tokens[masked_idx] = tokenizer.mask_token
print(tokens)  # output: ['[CLS]', '▁4', '年に', '1', '度', '[MASK]', 'は', '開かれる', '。']

# convert to ids
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print(token_ids)  # output: [4, 1602, 44, 24, 368, 6, 11, 21583, 8]

# convert to tensor
import torch
token_tensor = torch.LongTensor([token_ids])

# provide position ids explicitly
position_ids = list(range(0, token_tensor.size(1)))
print(position_ids)  # output: [0, 1, 2, 3, 4, 5, 6, 7, 8]
position_id_tensor = torch.LongTensor([position_ids])

# get the top 10 predictions of the masked token
with torch.no_grad():
    outputs = model(input_ids=token_tensor, position_ids=position_id_tensor)
    predictions = outputs[0][0, masked_idx].topk(10)

for i, index_t in enumerate(predictions.indices):
    index = index_t.item()
    token = tokenizer.convert_ids_to_tokens([index])[0]
    print(i, token)

"""
0 総会
1 サミット
2 ワールドカップ
3 フェスティバル
4 大会
5 オリンピック
6 全国大会
7 党大会
8 イベント
9 世界選手権
"""
~~~~

# Model architecture
A 12-layer, 768-hidden-size transformer-based masked language model.

# Training
The model was trained on [Japanese CC-100](http://data.statmt.org/cc-100/ja.txt.xz) and [Japanese Wikipedia](https://dumps.wikimedia.org/jawiki/) to optimize a masked language modelling objective on 8*V100 GPUs for around 15 days. It reaches ~3.9 perplexity on a dev set sampled from CC-100.

# Tokenization
The model uses a [sentencepiece](https://github.com/google/sentencepiece)-based tokenizer, the vocabulary was trained on the Japanese Wikipedia using the official sentencepiece training script.

# Licenese
[The MIT license](https://opensource.org/licenses/MIT)
