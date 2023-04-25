---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- astronomy
widget:
- text: a photo of the sun hbbltls astronomy
---

# DreamBooth model for the astronomy concept trained by Dhruv Singal on the NASA Astronomy Picture of the Week dataset.

This is a Stable Diffusion 2.1 model fine-tuned on the astronomy concept with DreamBooth. It can be used by modifying the `instance_prompt`: a photo of the solar system hbbltls astronomy****

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Example
![](download.png)

## Description


This is a Stable Diffusion model fine-tuned on NASA's Astronomy Picture of the Week images from the Hubble Telescope for the astronomy theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('alphatozeta/nasa-potw-hbbltls-astronomy')
image = pipeline().images[0]
image
```
