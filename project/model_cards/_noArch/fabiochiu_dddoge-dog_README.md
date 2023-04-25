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
- text: a photo of dddoge dog in the Acropolis
---

# DreamBooth model for the dddoge concept trained by fabiochiu on the fabiochiu/doge dataset.

This is a Stable Diffusion model fine-tuned on the dddoge concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of dddoge dog**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `dog` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('fabiochiu/dddoge-dog')
image = pipeline().images[0]
image
```
