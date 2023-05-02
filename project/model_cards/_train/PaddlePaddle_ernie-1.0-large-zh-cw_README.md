---
library_name: paddlenlp
license: apache-2.0
language:
- zh
tags:
- fill-mask
mask_token: "[MASK]"
---

[![paddlenlp-banner](https://user-images.githubusercontent.com/1371212/175816733-8ec25eb0-9af3-4380-9218-27c154518258.png)](https://github.com/PaddlePaddle/PaddleNLP)

# PaddlePaddle/ernie-1.0-large-zh-cw

## Introduction

We present a novel language representation model enhanced by knowledge called ERNIE (Enhanced Representation through kNowledge IntEgration). 
Inspired by the masking strategy of BERT, ERNIE is designed to learn language representation enhanced by knowledge masking strategies, 
which includes entity-level masking and phrase-level masking. Entity-level strategy masks entities which are usually composed of multiple words.
Phrase-level strategy masks the whole phrase which is composed of several words standing together as a conceptual unit.
Experimental results show that ERNIE outperforms other baseline methods, achieving new state-of-the-art results on five Chinese natural language processing tasks 
including natural language inference, semantic similarity, named entity recognition, sentiment analysis and question answering. 
We also demonstrate that ERNIE has more powerful knowledge inference capacity on a cloze test.

More detail: https://arxiv.org/abs/1904.09223

## Available Models

- ernie-1.0-base-zh
- ernie-1.0-large-zh-cw

## How to Use?

Click on the *Use in paddlenlp* button on the top right!

## Citation Info

```text
@article{ernie2.0,
  title = {ERNIE: Enhanced Representation through Knowledge Integration},
  author = {Sun, Yu and Wang, Shuohuan and Li, Yukun and Feng, Shikun and Chen, Xuyi and Zhang, Han and Tian, Xin and Zhu, Danxiang and Tian, Hao and Wu, Hua},
  journal={arXiv preprint arXiv:1904.09223},
  year = {2019},
}
```