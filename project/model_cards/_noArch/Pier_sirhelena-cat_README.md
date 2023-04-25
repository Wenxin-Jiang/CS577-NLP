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
- text: a photo of SirHelena black cat in front of the colosseo
---

# DreamBooth model for the SirHelena concept trained by Pier on the Pier/sirhelena-cat dataset.

This is a Stable Diffusion model fine-tuned on the SirHelena concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of SirHelena black cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `black cat` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Pier/sirhelena-cat')
image = pipeline().images[0]
image
```
