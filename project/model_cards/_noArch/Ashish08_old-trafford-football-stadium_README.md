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
datasets: Ashish08/old-trafford
widget:
- text: a photo of old-trafford football-stadium with a red sky
---

# DreamBooth model for the old-trafford concept trained by Ashish08 on the Ashish08/old-trafford dataset.

This is a Stable Diffusion model fine-tuned on the old-trafford concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of old-trafford football-stadium**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `football-stadium` images for the landscape theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Ashish08/old-trafford-football-stadium')
image = pipeline().images[0]
image
```
