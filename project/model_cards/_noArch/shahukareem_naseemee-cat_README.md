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
- text: A cute and adorable photo of naseemee cat
---

# DreamBooth model for the naseemee concept trained by shahukareem on the shahukareem/naseemee dataset.

This is a Stable Diffusion model fine-tuned on the naseemee concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of naseemee cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `cat` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('shahukareem/naseemee-cat')
image = pipeline().images[0]
image
```
