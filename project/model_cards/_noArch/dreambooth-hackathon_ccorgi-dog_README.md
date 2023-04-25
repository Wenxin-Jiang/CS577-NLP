---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- animal
widget:
- text: a photo of ccorgi dog in the Acropolis
---

# DreamBooth model for ccorgi trained by lewtun on the lewtun/corgi dataset.

This your the Stable Diffusion model fine-tuned the ccorgi concept taught to Stable Diffusion with DreamBooth.
It can be used by modifying the `instance_prompt`: **a photo of ccorgi dog**

This model was created as part of the DreamBooth Hackathon. Visit the organisation page for instructions on how to take part!

## Description

Describe your model and concept here.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('dreambooth-hackathon/ccorgi-dog')
image = pipeline().images[0]
image
```
