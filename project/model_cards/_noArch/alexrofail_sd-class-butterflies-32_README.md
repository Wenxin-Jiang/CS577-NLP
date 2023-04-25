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
In this run I just ran each cell of the NB to understand what is going on.
Experimentation to follow 🙏

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained(alexrofail/sd-class-butterflies-32)
image = pipeline().images[0]
image
```
