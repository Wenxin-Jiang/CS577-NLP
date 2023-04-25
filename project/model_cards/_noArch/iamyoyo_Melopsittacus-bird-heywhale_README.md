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
- text: A budgie is pictured with its eyes wide open
---

# DreamBooth model for the Melopsittacus concept trained by iamyoyo.

This is a Stable Diffusion model fine-tuned on the Melopsittacus concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of Melopsittacus bird**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `bird` images for the wildcard theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('iamyoyo/Melopsittacus-bird-heywhale')
image = pipeline().images[0]
image
```
