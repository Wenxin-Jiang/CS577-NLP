---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- animal
widget:
- text: a photo of sgengiuli dog in the Acropolis with a crocodile hidden behind
---

# DreamBooth model for the sgengiuli concept trained by DiTo97 on a private dataset of images of his childhood dog Leo (also known as *Sgengiuli*), which passed away in late 2020.

This is a Stable Diffusion model fine-tuned on the sgengiuli concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of sgengiuli dog**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `dog` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('DiTo97/sgengiuli-dog')
image = pipeline().images[0]
image
```
