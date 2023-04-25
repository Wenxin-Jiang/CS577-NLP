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
- text: a photo of rsanchez character in a spaceship
---

# DreamBooth model for the rsanchez concept trained by Kayvane on the Kayvane/dreambooth-hackathon-rick-and-morty-images-square dataset.

This is a Stable Diffusion model fine-tuned on the rsanchez concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of rsanchez character**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `character` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Kayvane/rick-and-morty-rsanchez-character-10000-steps-20-inputs')
image = pipeline().images[0]
image
```
