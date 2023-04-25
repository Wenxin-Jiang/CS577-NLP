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
- text: a professional photo of ppadseeew dish for christmas
---

# DreamBooth model for the ppadseeew concept trained by taesiri.

This is a Stable Diffusion model fine-tuned on the ppadseeew concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of ppadseeew dish**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `dish` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('taesiri/ppadseeew-dish')
image = pipeline().images[0]
image
```

## Sample Results

![sample-results](sample-image.png)
