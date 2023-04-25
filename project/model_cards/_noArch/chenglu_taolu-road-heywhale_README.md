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
- heywhale
widget:
- text: A Godzilla sleep on the taolu road, with a ps5 in it's hand
---

# DreamBooth model for the taolu concept trained by chenglu.

This is a Stable Diffusion model fine-tuned on the taolu concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of taolu road**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `road` images for the landscape theme. For the HF Dreambooth hackathon, from Hugging Face China Commuinity, Collabration with the HeyWhale platform.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('chenglu/taolu-road-heywhale')
image = pipeline().images[0]
image
```
