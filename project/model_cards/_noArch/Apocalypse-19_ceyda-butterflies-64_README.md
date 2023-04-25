---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

This model is a diffusion model for unconditional image generation of butterflies
trained on the ceyda smithsonian butterflies at a sample resolution of 64*64.

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('Apocalypse-19/ceyda-butterflies-64')
image = pipeline().images[0]
image
```
