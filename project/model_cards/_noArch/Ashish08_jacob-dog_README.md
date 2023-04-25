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
datasets: Ashish08/jacob-soni
widget:
- text: a photo of jacob dog sitting on a rock
---

# DreamBooth model for the jacob concept trained by Ashish08 on the Ashish08/jacob-soni dataset.

This is a Stable Diffusion model fine-tuned on the jacob concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of jacob dog**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `dog` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Ashish08/jacob-dog')
image = pipeline().images[0]
image
```
