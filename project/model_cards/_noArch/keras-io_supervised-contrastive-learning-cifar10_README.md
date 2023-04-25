---
library_name: keras
tags:
- image-classification
datasets:
- cifar10
license: apache-2.0
---
A classification model trained with <a href='https://arxiv.org/abs/2004.11362' target='_blank'>**Supervised Contrastive Learning**</a> (Prannay Khosla et al.).
The training procedure was done as seen in the example on <a href='https://keras.io/examples/vision/supervised-contrastive-learning/' target='_blank'>**keras.io**</a>  by Khalid Salama.

The model was **trained on cifar10**, which includes ten classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck.

The **test accuracy after 50 epochs** of the model with contrastive learning was **81.06%** (opposed to 79.88% without contrastive learning).