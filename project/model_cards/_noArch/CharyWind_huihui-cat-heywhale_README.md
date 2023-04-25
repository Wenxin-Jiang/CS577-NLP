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
- text: illustration of a huihui cat sitting on top of the deck of a battle ship traveling
    through the open sea with a lot of ships surrounding it
---

# DreamBooth model for the huihui concept trained by CharyWind.

This is a Stable Diffusion model fine-tuned on the huihui concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of huihui cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `cat` images for the wildcard theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('CharyWind/huihui-cat-heywhale')
image = pipeline().images[0]
image
```
