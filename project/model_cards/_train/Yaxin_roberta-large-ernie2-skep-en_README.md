---
language: en
---

# SKEP-Roberta

## Introduction

SKEP (SKEP: Sentiment Knowledge Enhanced Pre-training for Sentiment Analysis) is proposed by Baidu in 2020,

SKEP propose Sentiment Knowledge Enhanced Pre-training for sentiment analysis. Sentiment masking and three sentiment pre-training objectives are designed to incorporate various types of knowledge for pre-training model.

More detail: https://aclanthology.org/2020.acl-main.374.pdf

## Released Model Info

|Model Name|Language|Model Structure|
|:---:|:---:|:---:|
|skep-roberta-large| English |Layer:24, Hidden:1024, Heads:24|

This released pytorch model is converted from the officially released PaddlePaddle SKEP model and 
a series of experiments have been conducted to check the accuracy of the conversion.

- Official PaddlePaddle SKEP repo: 
  1. https://github.com/PaddlePaddle/PaddleNLP/blob/develop/paddlenlp/transformers/skep
  2. https://github.com/baidu/Senta
- Pytorch Conversion repo: Not released yet


## How to use
```Python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("Yaxin/roberta-large-ernie2-skep-en")
model = AutoModel.from_pretrained("Yaxin/roberta-large-ernie2-skep-en")
```

```
#!/usr/bin/env python
#encoding: utf-8
import torch
from transformers import RobertaTokenizer, RobertaForMaskedLM

tokenizer = RobertaTokenizer.from_pretrained('Yaxin/roberta-large-ernie2-skep-en')

input_tx = "<s> He like play with student, so he became a <mask> after graduation </s>"
# input_tx = "<s> He is a <mask> and likes to get along with his students </s>"

tokenized_text = tokenizer.tokenize(input_tx)
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)

tokens_tensor = torch.tensor([indexed_tokens])
segments_tensors = torch.tensor([[0] * len(tokenized_text)])

model = RobertaForMaskedLM.from_pretrained('Yaxin/roberta-large-ernie2-skep-en')
model.eval()

with torch.no_grad():
    outputs = model(tokens_tensor, token_type_ids=segments_tensors)
    predictions = outputs[0]

predicted_index = [torch.argmax(predictions[0, i]).item() for i in range(0, (len(tokenized_text) - 1))]
predicted_token = [tokenizer.convert_ids_to_tokens([predicted_index[x]])[0] for x in
                   range(1, (len(tokenized_text) - 1))]

print('Predicted token is:', predicted_token)
```
## Citation

```bibtex
@article{tian2020skep,
  title={SKEP: Sentiment knowledge enhanced pre-training for sentiment analysis},
  author={Tian, Hao and Gao, Can and Xiao, Xinyan and Liu, Hao and He, Bolei and Wu, Hua and Wang, Haifeng and Wu, Feng},
  journal={arXiv preprint arXiv:2005.05635},
  year={2020}
}

```

```
reference:
https://github.com/nghuyong/ERNIE-Pytorch

```