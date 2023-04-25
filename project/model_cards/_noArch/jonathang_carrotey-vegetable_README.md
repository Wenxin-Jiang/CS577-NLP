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
- text: a photo of carrotey vegetable in the Acropolis
---

# DreamBooth model for the carrotey concept trained by jonathang on the jonathang/dreambooth-hackathon-images dataset.

This is a Stable Diffusion model fine-tuned on the carrotey concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of carrotey vegetable**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `vegetable` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('jonathang/carrotey-vegetable')
image = pipeline().images[0]
image
```
