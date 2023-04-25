---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Stable Diffusion on Satellite Images

This model is a diffusion model for unconditional image generation of Sentinel-2 Images based on the EuroSAT Dataset.

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('nkasmanoff/sd-eurosat')
image = pipeline().images[0]
image
```
