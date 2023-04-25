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
- text: a photo of corgi in space nebulas
---

# DreamBooth model for the space concept trained by GeorgeBredis on the GeorgeBredis/dreambooth-hackathon-images dataset.

This is a Stable Diffusion model fine-tuned on the space concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of space nebulas**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `nebulas` images for the science theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('GeorgeBredis/space-nebulas')
image = pipeline().images[0]
image
```
