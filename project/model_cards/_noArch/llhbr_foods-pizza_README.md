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
- text: a photo of foods pizza on a plate, with a beer next to it, against a beach
    backdrop
---

# DreamBooth model for the foods concept trained by llhbr on the llhbr/dreamboot-pizza dataset.

This is a Stable Diffusion model fine-tuned on the foods concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of foods pizza**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `pizza` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('llhbr/foods-pizza')
image = pipeline().images[0]
image
```
