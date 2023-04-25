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
- text: Paint a sitar surrounded by objects and symbols that reflect the cultural
    and artistic influences of Salvador Dali
---

# DreamBooth model for the instrument concept trained by Someman on the Someman/Sitar dataset.

This is a Stable Diffusion model fine-tuned on the instrument concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of sitar**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `sitar` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Someman/sitar-psych')
image = pipeline().images[0]
image
```
