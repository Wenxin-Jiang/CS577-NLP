---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- landscape
widget:
- text: a photo of landscape ocean in the Acropolis
---

# DreamBooth model for the landscape concept trained by nahidalam on the nahidalam/landscape dataset.

This is a Stable Diffusion model fine-tuned on the landscape concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of landscape ocean**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `ocean` images for the landscape theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('nahidalam/landscape-ocean')
image = pipeline().images[0]
image
```
