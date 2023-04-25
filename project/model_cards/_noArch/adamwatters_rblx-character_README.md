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
- text: a photo of rblx character in front of statue of liberty
---

# DreamBooth model for the rblx concept trained by adamwatters on the adamwatters/roblox-guy dataset.

## Description

<figure>
<img src=https://datasets-server.huggingface.co/assets/adamwatters/roblox-guy/--/adamwatters--roblox-guy/train/7/image/image.jpg width=200px height=200px>
<figcaption align = "left"><b>Screenshot from Roblox used for training</b></figcaption>
</figure>

This is a Stable Diffusion model fine-tuned on images of my specific customized Roblox avatar. Idea is: maybe it would be fun for Roblox players to make images of their avatars in different settings.

It can be used by modifying the instance_prompt: a photo of rblx character

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Generate Images
<img src=https://huggingface.co/datasets/adamwatters/hosted-images/resolve/main/roblox-guy-grid.jpeg width=60%>

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('adamwatters/rblx-character')
image = pipeline().images[0]
image
```
