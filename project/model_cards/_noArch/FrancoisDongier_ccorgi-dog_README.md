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
datasets: lewtun/corgi
widget:
- text: a photo of ccorgi dog on a beautiful beach
---

# DreamBooth model for the ccorgi concept trained by FrancoisDongier on the lewtun/corgi dataset.

This is a Stable Diffusion model fine-tuned on the ccorgi concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of ccorgi dog**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `dog` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('FrancoisDongier/ccorgi-dog')
image = pipeline().images[0]
image
```
