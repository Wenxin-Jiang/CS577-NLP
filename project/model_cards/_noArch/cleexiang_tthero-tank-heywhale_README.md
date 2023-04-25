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
- text: illustration of a tthero tank sitting on top of the deck of a battle ship
    traveling through the open sea with a lot of ships surrounding it
---

# DreamBooth model for the tthero concept trained by cleexiang.

This is a Stable Diffusion model fine-tuned on the tthero concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of tthero tank**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `tank` images for the wildcard theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('cleexiang/tthero-tank-heywhale')
image = pipeline().images[0]
image
```
