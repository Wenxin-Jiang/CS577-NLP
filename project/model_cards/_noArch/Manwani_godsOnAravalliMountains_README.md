---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- landscape
widget:
- text: a viking north druid lich mermaid king wise old man god of death with thunder
    in his eyes standing on the Aravalli mountains
---

# DreamBooth model for the godsOnAravalliMountains concept trained by Manwani on the Manwani/AravalliMountains dataset.

This is a Stable Diffusion model fine-tuned on the Gods concept with DreamBooth. It can be used by modifying the `instance_prompt`: **Gods on Aravalli Mountains**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on aravalli mountains of my hometown Ajmer, which is an oldest cities in the Indian state of Rajasthan for the landscape theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Manwani/godsOnAravalliMountains')
image = pipeline().images[0]
image
```
