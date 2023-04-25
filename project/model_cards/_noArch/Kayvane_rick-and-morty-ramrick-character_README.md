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
widget:
- text: a photo of ramrick character as a pickle
---

# DreamBooth model for the ramrick concept trained by Kayvane on the Kayvane/dreambooth-hackathon-rick-and-morty-images-square dataset.

Notes:
- trained on square images, 20k steps on google colab
- character name is ramrick, many pictures get blocked as nsfw - possibly because the subtoken #ick is close to something else
- model is trained for too many steps / overfitted as it is effectively recreating the input images

This is a Stable Diffusion model fine-tuned on the ramrick concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of ramrick character**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `character` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Kayvane/rick-and-morty-ramrick-character')
image = pipeline().images[0]
image
```
