---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Model Card for Stable Diffusion - Butterflies, 32px
Model developed for the Unit 1 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class).

This model is a diffusion model for unconditional image generation of cute butterflies 🦋.  
It is trained on a very small collection of 1'000 pictures and trained for 30 epochs.

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('alkiskoudounas/sd-butterflies-32px')
image = pipeline().images[0]
image
```
