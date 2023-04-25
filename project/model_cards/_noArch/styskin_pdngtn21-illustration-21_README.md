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
- text: illustration owl on wood by pdngtn21
---

# DreamBooth model for the pdngtn21 concept trained by styskin on the styskin/paddington dataset.

This is a Stable Diffusion model fine-tuned on the pdngtn21 concept with DreamBooth. It can be used by modifying the `instance_prompt`: **illustration by pdngtn21**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `illustration` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('styskin/pdngtn21-illustration-21')
image = pipeline().images[0]
image
```
