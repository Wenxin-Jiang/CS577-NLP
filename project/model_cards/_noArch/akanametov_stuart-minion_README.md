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
datasets: akanametov/minions-dataset
widget:
- text: a photo of stuart minion on the Moon
---

# DreamBooth model for the stuart concept trained by akanametov on the akanametov/minions-dataset dataset.

This is a Stable Diffusion model fine-tuned on the stuart concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of stuart minion**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `minion` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('akanametov/stuart-minion')
image = pipeline().images[0]
image
```
