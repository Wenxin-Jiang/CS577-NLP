---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Model Card for Unit 1 of the [Diffusion Models Class]

This model is a diffusion model for unconditional image generation of butterflies

## Usage

```python
from diffusers import DDPMPipeline

pipelie = DDPMPipeline.from_pretrained('jaybeeja/sd-class-butterflies-64')
image = pipeline().images[0]
image
```
