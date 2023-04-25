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
- text: a big dog with danphe face
---

# DreamBooth model for the bird concept trained by Someman on the Someman/danphe dataset.

This is a Stable Diffusion model fine-tuned on the bird concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of bird danphe**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `danphe` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Someman/bird-danphe')
image = pipeline().images[0]
image
```
