---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
- butterfly-generation
datasets: ceyda/smithsonian_butterflies
---

This model is a diffusion model for unconditional image generation of butterflies
trained on the ceyda/smithsonian_butterflies dataset.

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('Apocalypse-19/sd-butterflies-ceyda-32')
image = pipeline().images[0]
image
```
