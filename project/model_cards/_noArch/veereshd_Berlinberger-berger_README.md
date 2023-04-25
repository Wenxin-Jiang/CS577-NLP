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
- text: a photo of Berlinberger berger in the city
---

# DreamBooth model for the Berlinberger concept trained by veereshd on the veereshd/Dreambooth_food_dataset dataset.

This is a Stable Diffusion model fine-tuned on the Berlinberger concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of Berlinberger berger**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `berger` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('veereshd/Berlinberger-berger')
image = pipeline().images[0]
image
```
