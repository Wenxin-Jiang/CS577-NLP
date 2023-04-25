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
widget:
- text: Van gogh painting boudhanath stupa
---

# DreamBooth model for the stupa concept trained by Someman on the Someman/boudhastupa dataset.

This is a Stable Diffusion model fine-tuned on the  concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of boudhanath stupa**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `boudhanath stupa` images for the landscape theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Someman/boudhanath-stupa')
image = pipeline().images[0]
image
```
