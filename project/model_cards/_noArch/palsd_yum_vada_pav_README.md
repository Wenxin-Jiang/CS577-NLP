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
- text: Eating yum_vada_pav vada pav with glass of chai while sitting at the bench
    in Antarctica in midst of glaciers
---

# DreamBooth model for the yum_vada_pav concept trained by palsd on the palsd/dreambooth_hackathon_vada_pav dataset.

This is a Stable Diffusion model fine-tuned on the yum_vada_pav concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of yum_vada_pav vada pav**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `vada pav` images for the food theme. Being foodie and Indian street foods lover, thought to play with stable diffusion model for Vada pav (Indian burger) images so I can enjoy dream of eating it in the midst of glaciers :)


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('palsd/yum_vada_pav')
image = pipeline().images[0]
image
```
