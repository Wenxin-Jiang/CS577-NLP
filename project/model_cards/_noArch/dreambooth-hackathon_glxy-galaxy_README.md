---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- science
widget:
- text: a photo of glxy galaxy
---

# DreamBooth model for glxy trained by lewtun on the lewtun/galaxies dataset.

This your the Stable Diffusion model fine-tuned the glxy concept taught to Stable Diffusion with DreamBooth.
It can be used by modifying the `instance_prompt`: **a photo of glxy galaxy**

This model was created as part of the DreamBooth Hackathon. Visit the organisation page for instructions on how to take part!

## Description

Describe your model and concept here.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('dreambooth-hackathon/glxy-galaxy')
image = pipeline().images[0]
image
```
