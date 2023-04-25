---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Model Card for Stable Diffusion - Aurora Borealis, 128px
Model developed for the Unit 1 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class).

This model is a diffusion model for unconditional image generation of aurora borealis 🌌.  
It is trained on a small collection of aurora pictures and trained for 50 epochs, with 🤗 Accelerate.

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('alkiskoudounas/sd-aurora-128px')
image = pipeline().images[0]
image
```

## Example
Here you can find an example of the output of the model, in a batch of 8 images:

![Butterflies Example](aurora-borealis-128px-examples.png)
