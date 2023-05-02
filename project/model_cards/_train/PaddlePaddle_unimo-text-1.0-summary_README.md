---
library_name: paddlenlp
license: apache-2.0
tags:
- summarization
language:
- zh
---

[![paddlenlp-banner](https://user-images.githubusercontent.com/1371212/175816733-8ec25eb0-9af3-4380-9218-27c154518258.png)](https://github.com/PaddlePaddle/PaddleNLP)

# PaddlePaddle/unimo-text-1.0-summary

## Introduction

Existed pre-training methods either focus on single-modal tasks or multi-modal tasks, and cannot effectively adapt to each other. 
They can only utilize single-modal data (i.e. text or image) or limited multi-modal data (i.e. image-text pairs). 
In this work, we propose a unified-modal pre-training architecture, namely UNIMO, which can effectively adapt to both single-modal and multi-modal 
understanding and generation tasks. Large scale of free text corpus and image collections can be utilized to improve the capability of visual 
and textual understanding, and cross-modal contrastive learning (CMCL) is leveraged to align the textual and visual information into a unified 
semantic space over a corpus of image-text pairs. As the non-paired single-modal data is very rich, our model can utilize much larger scale of 
data to learn more generalizable representations. Moreover, the textual knowledge and visual knowledge can enhance each other in the unified semantic space. 
The experimental results show that UNIMO significantly improves the performance of several single-modal and multi-modal downstream tasks.

More detail: https://arxiv.org/abs/2012.15409

## Available Models

- **unimo-text-1.0**, *12 layer, 12 heads, 768 hidden size, pretrained model*
- **unimo-text-1.0-large**, *24 layer, 16 heads, 1024 hidden size, pretrained model*
- **unimo-text-1.0-lcsts-new**, *12 layer, 12 heads, 768 hidden size, finetuned on the lcsts-new Chinese summarization dataset*
- **unimo-text-1.0-summary**, *12 layer, 12 heads, 768 hidden size, finetuned on several in-house Chinese summarization datasets*

## How to Use?

Click on the *Use in paddlenlp* button on the top right!

## Citation Info

```text
@article{ernie2.0,
  title = {UNIMO: Towards Unified-Modal Understanding and Generation via Cross-Modal Contrastive Learning},
  author = {Li, Wei and Gao, Can and Niu, Guocheng and Xiao, Xinyan and Liu, Hao and Liu, Jiachen and Wu, Hua and Wang, Haifeng},
  journal={arXiv preprint arXiv:2012.15409},
  year = {2020},
}
```

