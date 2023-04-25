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
- text: a photo of a beautiful anime city in vioeva style
---

# DreamBooth model for the vioeva concept trained by Antiraedus on the Antiraedus/Violet-Evergarden dataset.
I FORGOT IT WAS GRAYSCALED

This is a Stable Diffusion model fine-tuned on the vioeva concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of a girl in vioeva style**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description
Violet Evergarden!!!!
Dataset [is located here](https://huggingface.co/datasets/Antiraedus/Violet-Evergarden)


This is a Stable Diffusion model fine-tuned on `style` images for the wildcard theme.


## Examples
"a photo of a beautiful anime city in vioeva style"
![](output_imgs.png)

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Antiraedus/Violet-Evergarden-Style')
image = pipeline().images[0]
image
```
