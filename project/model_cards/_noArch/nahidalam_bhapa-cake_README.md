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
- text: Trump eating bhapa cake
---

# DreamBooth model for the bhapa concept trained by nahidalam on the nahidalam/bhapa dataset.

This is a Stable Diffusion model fine-tuned on the bhapa concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of bhapa cake**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `cake` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('nahidalam/bhapa-cake')
image = pipeline().images[0]
image
```
