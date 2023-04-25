---
license: apache-2.0
tags:
- image-classification
datasets:
- imagenet
---

# VAN-Tiny

VAN is trained on ImageNet-1k (1 million images, 1,000 classes) at resolution 224x224. It was first introduced in the paper [Visual Attention Network](https://arxiv.org/abs/2202.09741) and first released in [here](https://github.com/Visual-Attention-Network). 


## Description

While originally designed for natural language processing (NLP) tasks, the self-attention mechanism has recently taken various computer vision areas by storm. However, the 2D nature of images brings three challenges for applying self-attention in computer vision. (1) Treating images as 1D sequences neglects their 2D structures. (2) The quadratic complexity is too expensive for high-resolution images. (3) It only captures spatial adaptability but ignores channel adaptability. In this paper, we propose a novel large kernel attention (LKA) module to enable self-adaptive and long-range correlations in self-attention while avoiding the above issues. We further introduce a novel neural network based on LKA, namely Visual Attention Network (VAN). While extremely simple and efficient, VAN outperforms the state-of-the-art vision transformers (ViTs) and convolutional neural networks (CNNs) with a large margin in extensive experiments, including image classification, object detection, semantic segmentation, instance segmentation, etc.

## Evaluation Results

| Model     | #Params(M) | GFLOPs | Top1 Acc(%) |                           Download                           |
| :-------- | :--------: | :----: | :---------: | :----------------------------------------------------------: |
| VAN-Tiny  |    4.1     |  0.9   |    75.4     |[Hugging Face 🤗](https://huggingface.co/Visual-Attention-Network/VAN-Tiny) |
| VAN-Small |    13.9    |  2.5   |    81.1     |[Hugging Face 🤗](https://huggingface.co/Visual-Attention-Network/VAN-Small) |
| VAN-Base  |    26.6    |  5.0   |    82.8     |[Hugging Face 🤗](https://huggingface.co/Visual-Attention-Network/VAN-Base), |
| VAN-Large |    44.8    |  9.0   |    83.9     |[Hugging Face 🤗](https://huggingface.co/Visual-Attention-Network/VAN-Large) |


### BibTeX entry and citation info
```bibtex
@article{guo2022visual,
  title={Visual Attention Network},
  author={Guo, Meng-Hao and Lu, Cheng-Ze and Liu, Zheng-Ning and Cheng, Ming-Ming and Hu, Shi-Min},
  journal={arXiv preprint arXiv:2202.09741},
  year={2022}
}
```