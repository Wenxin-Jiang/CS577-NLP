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
- text: Beautiful landscape of mworld
---

# DreamBooth model for the mworld concept trained by jonathang on the jonathang/dreambooth-hackathon-images-mario-bg-1 dataset.

This is a Stable Diffusion model fine-tuned on the mworld concept with DreamBooth. It can be used by modifying the `instance_prompt`: **mworld**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `` images for the landscape theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('jonathang/mworld')
image = pipeline().images[0]
image
```
