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
- text: a photo of mimicat cat wearing a santa hat
---

# DreamBooth model for the mimicat concept trained by mjfang27 on the mjfang27/dreambooth-hackathon-images dataset.

This is a Stable Diffusion model fine-tuned on the mimicat concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of mimicat cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `cat` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('mjfang27/mimicat-cat')
image = pipeline().images[0]
image
```
