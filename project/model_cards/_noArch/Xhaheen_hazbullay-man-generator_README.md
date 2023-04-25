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
- text: a photo of hazbullay man with the Statue of Zeus from Ancient Greece in the
    background
---

# DreamBooth model for the hazbullay concept trained by Xhaheen on the bethecloud/golf-courses dataset.

This is a Stable Diffusion model fine-tuned on the hazbullay concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of hazbullay man**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `man` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Xhaheen/hazbullay-man-generator')
image = pipeline().images[0]
image
```
