---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

This model is a diffusion model for unconditional image generation of bored apes 🦧.

## Usage

```python
from diffusers import DDPMPipeline

# run pipeline in inference (sample random noise and denoise)
pipeline = DDPMPipeline.from_pretrained('CCMat/diff-bored-apes-64')
image = pipeline().images[0]

# save image
image.save("ddpm_generated_image.png")
```

## Samples
![example images](bored-apes-grid.png)