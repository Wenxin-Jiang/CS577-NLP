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
- text: a photo of pishicat cat at the scene of JFKs assassination
---

# DreamBooth model for the pishicat concept trained by Atallahw on the Atallahw/pishi2 dataset.

This is a Stable Diffusion model fine-tuned on the pishicat concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of pishicat cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `cat` images for the animal theme. It makes images of my cat.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Atallahw/mycatPishi')
image = pipeline().images[0]
image
```
