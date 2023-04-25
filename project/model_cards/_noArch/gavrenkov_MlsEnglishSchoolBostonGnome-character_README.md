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
- text: a photo of MlsEnglishSchoolBostonGnome character in the Acropolis
---

# DreamBooth model for the MlsEnglishSchoolBostonGnome concept trained by gavrenkov on the gavrenkov/MLSGnome dataset.

This is a Stable Diffusion model fine-tuned on the MlsEnglishSchoolBostonGnome concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of MlsEnglishSchoolBostonGnome character**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `character` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('gavrenkov/MlsEnglishSchoolBostonGnome-character')
image = pipeline().images[0]
image
```
