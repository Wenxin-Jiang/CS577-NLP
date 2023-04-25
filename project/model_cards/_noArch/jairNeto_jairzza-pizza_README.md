---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- food
widget:
- text: a photo of jairzza pizza in the Acropolis
---

# DreamBooth model for the jairzza concept trained by jairNeto on the jairNeto/pizza dataset.

This is a Stable Diffusion model fine-tuned on the jairzza concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of jairzza pizza**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `pizza` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('jairNeto/jairzza-pizza')
image = pipeline().images[0]
image
```
