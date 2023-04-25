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
datasets: juancopi81/home-office-jcp
widget:
- text: a photo of Bill Gates smiling, working at a jcphomeoffice office
---

# DreamBooth model for the jcphomeoffice concept trained by juancopi81 on the juancopi81/home-office-jcp dataset.

This is a Stable Diffusion model fine-tuned on the jcphomeoffice concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of jcphomeoffice office**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `office` images for the landscape theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('juancopi81/jcphomeoffice-office')
image = pipeline().images[0]
image
```
