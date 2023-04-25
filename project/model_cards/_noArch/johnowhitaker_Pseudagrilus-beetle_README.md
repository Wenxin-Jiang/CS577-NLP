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
- text: a photo of Pseudagrilus beetle underwater
---

# DreamBooth model for Pseudagrilus trained by johnowhitaker on the johnowhitaker/Pseudagrilus dataset.

This is a Stable Diffusion model fine-tuned the Pseudagrilus concept taught to Stable Diffusion with DreamBooth.
It can be used by modifying the `instance_prompt`: **a photo of Pseudagrilus beetle**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `beetle` images for the animal theme. (test run)


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('johnowhitaker/Pseudagrilus-beetle')
image = pipeline().images[0]
image
```
