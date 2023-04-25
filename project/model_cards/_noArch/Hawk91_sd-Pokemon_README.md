---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---
# Model Card for Unit 1 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class)

If you are wondering what would happen when a model trained on a bunch of images pokemons and then denoising them using Diffusion, then check out this model.

## Usage

```python
from diffusers import DDPMPipeline
pipeline = DDPMPipeline.from_pretrained('Hawk91/sd-Pokemon')
image = pipeline().images[0]
image
```