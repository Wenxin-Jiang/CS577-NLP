---
license: apache-2.0
language:
  - zh
library_name: paddlenlp
tags:
  - conversational
---

[![paddlenlp-banner](https://user-images.githubusercontent.com/1371212/175816733-8ec25eb0-9af3-4380-9218-27c154518258.png)](https://github.com/PaddlePaddle/PaddleNLP)

# PaddlePaddle/plato-mini

## Introduction

Pre-training models have been proved effective for a wide range of natural language processing tasks. 
Inspired by this, we propose a novel dialogue generation pre-training framework to support various kinds of conversations, 
including chit-chat, knowledge grounded dialogues, and conversational question answering. In this framework, we adopt flexible 
attention mechanisms to fully leverage the bi-directional context and the uni-directional characteristic of language generation. 
We also introduce discrete latent variables to tackle the inherent one-to-many mapping problem in response generation. 
Two reciprocal tasks of response generation and latent act recognition are designed and carried out simultaneously within a shared network. 
Comprehensive experiments on three publicly available datasets verify the effectiveness and superiority of the proposed framework.

More detail: https://arxiv.org/abs/1910.07931

## Available Models

- **plato-mini**, *6 layer, 12 heads, 768 hidden size*

## How to Use?

Click on the *Use in paddlenlp* button on the top right!

## Citation Info

```text
@article{ernie2.0,
  title = {PLATO: Pre-trained Dialogue Generation Model with Discrete Latent Variable},
  author = {Bao, Siqi and He, Huang and Wang, Fan and Wu, Hua and Wang, Haifeng},
  journal={arXiv preprint arXiv:1910.07931},
  year = {2019},
}
```


