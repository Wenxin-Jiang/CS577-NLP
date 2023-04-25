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
- text: a photo of kyoto deers in line
---

# DreamBooth model for the kyoto concept trained by bobber on the bobber/dreambooth-hackathon-images dataset.

This is a Stable Diffusion model fine-tuned on the kyoto concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of kyoto deer**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `deer` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('bobber/kyoto-deer')
image = pipeline().images[0]
image
```
