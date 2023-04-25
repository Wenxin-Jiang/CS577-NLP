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
- text: a photo of a white wbchaop wallbed
---

# DreamBooth model for the wbchaop concept trained by dadosdq on the dadosdq/wallbed_dataset dataset.

This is a Stable Diffusion model fine-tuned on the wbchaop concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of wbchaop wallbed**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `wallbed` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('dadosdq/wbchaop-wallbed')
image = pipeline().images[0]
image
```
