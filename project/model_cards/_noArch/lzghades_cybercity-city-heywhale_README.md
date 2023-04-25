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
- text: illustration of a cybercity city
---

# DreamBooth model for the cybercity concept trained by lzghades.

This is a Stable Diffusion model fine-tuned on the cybercity concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of cybercity city**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `city` images for the wildcard theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('lzghades/cybercity-city-heywhale')
image = pipeline().images[0]
image
```
