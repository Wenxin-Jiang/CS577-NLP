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
- text: a photo of sinha rock in the Kingdom of Greece
---

# DreamBooth model for the sinha (Sigiriya rock) concept trained by hasarinduperera on the hasarinduperera/sigiriya-image-dataset dataset.

This is a Stable Diffusion model fine-tuned on the sinha (Sigiriya rock) concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of sinha rock**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on Sigiriya `rock` images for the landscape theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('hasarinduperera/sinha-rock')
image = pipeline().images[0]
image
```
