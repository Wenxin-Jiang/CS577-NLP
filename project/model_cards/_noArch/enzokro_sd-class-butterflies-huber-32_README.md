---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Model Card for Unit 1 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class)

This model is a diffusion model for unconditional image generation of cute 🦋.  

It was trained with a SmoothL1 loss with Beta = 1 (aka same as Huber Loss).

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('enzokro/sd-class-butterflies-huber-32')
image = pipeline().images[0]
image
```
