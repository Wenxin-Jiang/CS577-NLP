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
widget:
- text: illustration of girl with brown bob haircut hugging west highland white terrier
    in Acropolis by pdngtn
---

# DreamBooth model for the pdngtn concept trained by styskin on the styskin/paddington dataset.

This is a Stable Diffusion model fine-tuned on the pdngtn concept with DreamBooth. It can be used by modifying the `instance_prompt`: **illustration by pdngtn**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `illustration` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('styskin/pdngtn-illustration')
image = pipeline().images[0]
image
```
