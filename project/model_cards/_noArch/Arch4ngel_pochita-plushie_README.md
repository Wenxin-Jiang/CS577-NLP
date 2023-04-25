---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- wildcard
datasets: Arch4ngel/pochita
widget:
- text: a photo of pochita plushie in the cosmos
---

# DreamBooth model for the pochita concept trained by Arch4ngel on the Arch4ngel/pochita dataset.

This is a Stable Diffusion model fine-tuned on the pochita concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of pochita plushie**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


Stable Diffusion model fine-tuned for generating Pochita plushie images.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Arch4ngel/pochita-plushie')
image = pipeline().images[0]
image
```
