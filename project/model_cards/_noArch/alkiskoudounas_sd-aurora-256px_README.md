---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Model Card for Stable Diffusion - Aurora Borealis, 256px
Model developed for the Unit 1 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class).

This model is a diffusion model for unconditional image generation of Aurora Borealis 🌌.  
It is trained on a small collection of aurora pictures and trained for 50 epochs, with 🤗 Accelerate.

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('alkiskoudounas/sd-aurora-256px')

```

## Example
Here you can find an example of the output of the model, in a batch of 8 images:

![Aurora Borealis Example](aurora-borealis-256px-examples.png)

