---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Model Card for Unit 1 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class)

This model is a diffusion model for unconditional image generation of Ukiyo-e images ✍ 🎨.
More about the dataset used: https://huggingface.co/datasets/huggan/ukiyoe2photo

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('alkzar90/sd-class-ukiyo-e-32')
image = pipeline().images[0]
image
```
