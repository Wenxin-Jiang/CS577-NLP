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
datasets: gstaff/okawari-style
widget:
- text: okawaristyle astronaut portrait with flowers and eagle on shoulder
---

# DreamBooth model for the okawaristyle concept trained by gstaff on the gstaff/okawari-style dataset.

This is a Stable Diffusion model fine-tuned on the okawaristyle concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of okawaristyle portrait**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `portrait` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('gstaff/okawaristyle-portrait')
image = pipeline().images[0]
image
```
