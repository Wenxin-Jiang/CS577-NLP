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
- text: illustration of a flyfood pet sit behind presendient trump
---

# DreamBooth model for the flyfood concept trained by innovation64.

This is a Stable Diffusion model fine-tuned on the flyfood concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of flyfood pet**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `派蒙` images for the wildcard theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('innovation64/flyfood-pet-heywhale')
image = pipeline().images[0]
image
```
