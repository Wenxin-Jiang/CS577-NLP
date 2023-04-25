---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- food
widget:
- text: a photo of sichuan cuisine in the Acropolis
---

# ==> Please ❤ Star ❤ if it helps <==

# DreamBooth model for the sichuan concept trained by loveunk on the loveunk/sichuan_cuisine dataset.

This is a Stable Diffusion model fine-tuned on the sichuan concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of sichuan cuisine**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `cuisine` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('loveunk/sichuan-cuisine')
image = pipeline().images[0]
image
```
