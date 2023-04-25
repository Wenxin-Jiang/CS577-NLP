---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- science
widget:
- text: a photo of cms cosmos
---

# DreamBooth model for cms trained by carlosabadia.

This is a Stable Diffusion model fine-tuned on the cms concept with DreamBooth. It can be used by modifying the `instance_prompt`: **cms cosmos**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on `cosmos` images for the science theme.

<img src=https://i.imgur.com/UsQ9BVi.jpg width=70% height=70%>

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('carlosabadia/cosmos')
image = pipeline().images[0]
image
```
