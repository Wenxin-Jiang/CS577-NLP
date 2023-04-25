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
- text: a photo of rio cat in the Acropolis
---

# DreamBooth model for the rio concept trained by marshmellow77 on the marshmellow77/pics_rio dataset.

This is a Stable Diffusion model fine-tuned on the rio concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of rio cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `cat` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('marshmellow77/rio-cat')
image = pipeline().images[0]
image
```
