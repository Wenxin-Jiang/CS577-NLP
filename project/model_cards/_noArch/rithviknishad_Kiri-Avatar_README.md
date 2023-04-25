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
---

# DreamBooth model for the Kiri concept trained by rithviknishad on the rithviknishad/kiri dataset.

This is a Stable Diffusion model fine-tuned on the Kiri concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of Kiri Avatar**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `Avatar` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('rithviknishad/Kiri-Avatar')
image = pipeline().images[0]
image
```
