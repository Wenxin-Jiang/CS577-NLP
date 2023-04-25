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
- text: a photo of markhor goat in the Acropolis
---

# DreamBooth model for the markhor concept trained by ihanif on the ihanif/markhor-images dataset.

This is a Stable Diffusion model fine-tuned on the markhor concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of markhor goat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `goat` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('ihanif/markhor-goat')
image = pipeline().images[0]
image
```
