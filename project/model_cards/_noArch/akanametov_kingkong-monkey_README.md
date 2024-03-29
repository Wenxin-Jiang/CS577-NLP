---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- animal
datasets: akanametov/kingkong-dataset
widget:
- text: a photo of kingkong monkey in the London
---

# DreamBooth model for the kingkong concept trained by akanametov on the akanametov/kingkong-dataset dataset.

This is a Stable Diffusion model fine-tuned on the kingkong concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of kingkong monkey**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `monkey` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('akanametov/kingkong-monkey')
image = pipeline().images[0]
image
```
