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
widget:
- text: illustration of a beautiful shiponsky ship
---

# DreamBooth model for the shiponsky concept trained by guofei1989.

This is a Stable Diffusion model fine-tuned on the shiponsky concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of shiponsky wildcard**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `wildcard` images for the wildcard theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('guofei1989/shiponsky-wildcard-heywhale')
image = pipeline().images[0]
image
```
