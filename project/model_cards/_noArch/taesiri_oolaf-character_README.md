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
- text: a professional photo of oolaf character for christmas
---

# DreamBooth model for the oolaf concept trained by taesiri.

This is a Stable Diffusion model fine-tuned on the oolaf concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of oolaf character**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `character` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('taesiri/oolaf-character')
image = pipeline().images[0]
image
```

## Sample image
![sample results](sample-image.png)
