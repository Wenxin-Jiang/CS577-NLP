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
- text: an ött3r otter flying over a city at night, neon lights, highly detailed,
    digital painting, artstation, concept art, sharp focus, illustration, art by artgerm
    and greg rutkowski and alphonse mucha, cinematic lighting
---

# DreamBooth model for the ött3r concept trained by mathpn on the mathpn/LeonardTheOtter dataset.

This is a Stable Diffusion model fine-tuned on the ött3r concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of ött3r otter**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `otter` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('mathpn/dreambooth-friendly-otter')
image = pipeline().images[0]
image
```
