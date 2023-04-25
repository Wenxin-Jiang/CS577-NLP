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
- text: a photo of an elephant in dota style
---

# DreamBooth model for the dota concept trained by Ducco on the Ducco/dota2style dataset.

This is a Stable Diffusion model fine-tuned on the dota concept with DreamBooth. It can be used by modifying the `instance_prompt`: **dota style**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `dota-style` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Ducco/dota-style')
image = pipeline().images[0]
image
```
