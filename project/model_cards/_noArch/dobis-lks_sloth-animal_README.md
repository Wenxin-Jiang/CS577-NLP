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
- text: a photo of sloth animal in the Acropolis
---

# DreamBooth model for the sloth concept trained by dobis-lks on the dobis-lks/test dataset.

This is a Stable Diffusion model fine-tuned on the sloth concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of sloth animal**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `animal` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('dobis-lks/sloth-animal')
image = pipeline().images[0]
image
```
