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
- text: a ultradetailed beautiful panting of a stylish arckt rocket launch, with smoke,
    and flames,, by conrad roset, greg rutkowski and makoto shinkai, trending on artstation
---

# DreamBooth model for the arckt concept trained by patrickfleith on the patrickfleith/dreambooth-hackathon-images-arckt dataset.

This is a Stable Diffusion model fine-tuned on the arckt (Ariane 5 rocket) concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of arckt rocket**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `Ariane5` rocket images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('patrickfleith/arckt-rocket-v0.1')
image = pipeline().images[0]
image
```
