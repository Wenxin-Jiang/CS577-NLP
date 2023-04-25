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
- text: photograph of catty pet sleeping soundly on a big soft bed with eyes closed
---

# DreamBooth model for the catty concept trained by Harukanaa.

This is a Stable Diffusion model fine-tuned on the catty concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of catty pet**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `pet` images for the animal theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
This is just my sleppy cat cattty, enjoy.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Harukanaa/catty-pet-heywhale')
image = pipeline().images[0]
image
```
