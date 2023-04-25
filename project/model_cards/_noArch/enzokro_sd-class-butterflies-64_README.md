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

The model was trained with Adam parameters from fast.ai.
Batch size was also doubled to 64.
Learning rate happens over 160 steps, aka 20% of training. 

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('enzokro/sd-class-butterflies-64')
image = pipeline().images[0]
image
```
