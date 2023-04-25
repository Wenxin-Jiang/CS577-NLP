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
- text: a photo of LeDude dog in the Acropolis
---

# DreamBooth model for the LeDude concept trained by Antiraedus on the Antiraedus/Dude dataset.

This is a Stable Diffusion model fine-tuned on the LeDude concept with DreamBooth, which is my 10 year old Australian Silky terrier.

It can be used by modifying the `instance_prompt`: **a photo of LeDude dog**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on `dog` images for the animal theme.

## Original
![](example_og.jpg)
## Example
![](example.png)
## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Antiraedus/LeDude-dog')
image = pipeline().images[0]
image
```
