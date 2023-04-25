---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- landscape
widget:
- text: a photo of swalps mountains
---

# DreamBooth model for swalps trained by lewtun on the lewtun/alps dataset.

This your the Stable Diffusion model fine-tuned the swalps concept taught to Stable Diffusion with DreamBooth.
It can be used by modifying the `instance_prompt`: **a photo of swalps mountains**

This model was created as part of the DreamBooth Hackathon. Visit the organisation page for instructions on how to take part!

## Description

Describe your model and concept here.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('dreambooth-hackathon/swalps-mountains')
image = pipeline().images[0]
image
```
