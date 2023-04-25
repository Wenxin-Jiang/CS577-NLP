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
- text: a photo of kndrtycr toy at the beach, hyper-realistic, 4k
---

# DreamBooth model for the kndrtycr concept trained by alikanakar on the alikanakar/sd_finetune_toy_car dataset.

This is a Stable Diffusion model fine-tuned on the kndrtycr concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of kndrtycr toy**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `toy` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('alikanakar/kndrtycr-toy')
image = pipeline().images[0]
image
```
