---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- wildcard
widget:
- text: illustration of a dashdash toy sitting on top of the deck of a battle ship
    traveling through the open sea with a lot of ships surrounding it
---

# DreamBooth model for the dashdash concept trained by xianbao.

This is a Stable Diffusion model fine-tuned on the dashdash concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of dashdash toy**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `toy` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('xianbao/dashdash-toy-heywhale-3')
image = pipeline().images[0]
image
```
