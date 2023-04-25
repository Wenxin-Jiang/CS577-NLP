---
language: 
  - en

thumbnail:

tags:
- keras
- tensorflow
- image-classification

library_name: generic
libraries: TensorBoard
license: apache-2.0
metrics:
- accuracy
model-index:
- name: Image-Classification-using-EANet
  results:
  - task: 
      type: Image-Classification-using-EANet
    dataset:
      type: Image
      name: CIFAR100
    metrics:
    - type: accuracy
      value: []
    - type: validation loss
      value: [] 
---

## Image-Classification-using-EANet with Keras

This repo contains the model and the notebook on [Image Classification using EANet with Keras](https://keras.io/examples/vision/eanet/).

Credits: [ZhiYong Chang](https://github.com/czy00000) - Original Author

HF Contribution: [Drishti Sharma](https://huggingface.co/spaces/DrishtiSharma)  


### Introduction

This example implements the EANet model for image classification, and demonstrates it on the [CIFAR-100](https://huggingface.co/datasets/cifar100) dataset. EANet introduces a novel attention mechanism named external attention, based on two external, small, learnable, and shared memories, which can be implemented easily by simply using two cascaded linear layers and two normalization layers. It conveniently replaces self-attention as used in existing architectures. External attention has linear complexity, as it only implicitly considers the correlations between all samples. 


### Implemention of the EANet model

The EANet model leverages external attention. The computational complexity of traditional self attention is O(d * N ** 2), where d is the embedding size, and N is the number of patch. The authors find that most pixels are closely related to just a few other pixels, and an N-to-N attention matrix may be redundant. So, they propose as an alternative an external attention module where the computational complexity of external attention is O(d * S * N). As d and S are hyper-parameters, the proposed algorithm is linear in the number of pixels. In fact, this is equivalent to a drop patch operation, because a lot of information contained in a patch in an image is redundant and unimportant.