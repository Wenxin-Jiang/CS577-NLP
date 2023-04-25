---
license: mit
tags:
- unconditional-image-generation
---
Fashion MNIST unconditional Unet Model trained using DDPM

Model Hyperparams:

- Model size: 51,834,625 params
- 3 stages: 128, 256, 512 channels
- Linear Attention in 2nd and 3rd stages, Self Attention in Middle Stage
- Optimizer: Adam
- LR: 3e-4
- Batch Size: 64
- Grad Accumulation: 8 steps
- Effectibe Batch Size: 512
- Total steps: 5,000
- Linear Beta Schedule: 1000 Steps

![output.png](https://s3.amazonaws.com/moonup/production/uploads/1672153152960-6262d89f63f73be3d2f6b7c1.png)