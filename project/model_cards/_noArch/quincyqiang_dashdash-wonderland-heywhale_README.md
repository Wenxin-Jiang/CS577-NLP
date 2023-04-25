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
- text: wonderland，trees
---

# DreamBooth model for the dashdash concept trained by quincyqiang.

This is a Stable Diffusion model fine-tuned on the dashdash concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of dashdash wonderland**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `wonderland` images for the wildcard theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('quincyqiang/dashdash-wonderland-heywhale')
image = pipeline().images[0]
image
```
