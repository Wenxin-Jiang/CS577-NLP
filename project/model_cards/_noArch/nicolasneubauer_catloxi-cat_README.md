---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon-notyet
- animal
widget:
- text: a renaissance painting of catloxi cat wearing a crown sitting on a throne,
    elegant, close-up
---

# DreamBooth model for the catloxi concept trained by nicolasneubauer on the nicolasneubauer/loxi dataset.

This is a Stable Diffusion model fine-tuned on the catloxi concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of catloxi cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `cat` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('nicolasneubauer/catloxi-cat')
image = pipeline().images[0]
image
```
