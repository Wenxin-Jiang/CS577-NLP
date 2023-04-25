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
- text: a photo of biriyani food an italian restaurant
---

# DreamBooth model for the biriyani concept trained by ashiqabdulkhader on the ashiqabdulkhader/Biriyani dataset.

This is a Stable Diffusion model fine-tuned on the biriyani concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of biriyani food**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `food` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('ashiqabdulkhader/biriyani-food')
image = pipeline().images[0]
image
```
