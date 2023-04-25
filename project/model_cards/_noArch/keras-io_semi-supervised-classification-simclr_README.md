---
library_name: keras
tags:
- image-classification
datasets:
- STL-10
license: apache-2.0
---
# Semi-supervised image classification using contrastive pretraining with SimCLR

## Description

This is a simple image classification model trained with **Semi-supervised image classification using contrastive pretraining with SimCLR**
The training procedure was done as seen in the example on <a href='https://keras.io/examples/vision/semisupervised_simclr/' target='_blank'>**keras.io**</a>  by András Béres.

The model was **trained on STL-10**, which includes ten classes: airplane, bird, car, cat, deer, dog, horse, monkey, ship, truck.

## Metrics
There is a public W&B dashboard available <a href='https://wandb.ai/johko-cel/semi-supervised-contrastive-learning-simclr'>here</a> which illustrates the difference in different metrics such as accuracy of a baseline supervised trained model, a purely unsupervised model (pretrain) and the supervised finetuned model based on the unsupervised.

## Background
(by András Béres on <a href='https://keras.io/examples/vision/semisupervised_simclr/' target='_blank'>**keras.io**</a> )
Semi-supervised learning is a machine learning paradigm that deals with partially labeled datasets. When applying deep learning in the real world, one usually has to gather a large dataset to make it work well. However, while the cost of labeling scales linearly with the dataset size (labeling each example takes a constant time), model performance only scales sublinearly with it. This means that labeling more and more samples becomes less and less cost-efficient, while gathering unlabeled data is generally cheap, as it is usually readily available in large quantities.

Semi-supervised learning offers to solve this problem by only requiring a partially labeled dataset, and by being label-efficient by utilizing the unlabeled examples for learning as well.

In this example, I pretrained an encoder with contrastive learning on the STL-10 semi-supervised dataset using no labels at all, and then fine-tuned it using only its labeled subset.