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
- text: a photo of britazzleshorg cat at Shakespeare outdoor amphitheater in pet costume
---

# DreamBooth model for the britazzleshorg concept trained by Nlpeva on the Nlpeva/British_shorthair dataset.

This is a Stable Diffusion model fine-tuned on the britazzleshorg concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of britazzleshorg cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `cat` images for the animal theme. It is based on ten images of a british shorthair.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Nlpeva/britazzleshorg-cat')
image = pipeline().images[0]
image
```
