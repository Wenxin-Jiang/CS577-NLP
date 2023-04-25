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
datasets: misza222/dreambooth-hackathon-Daphnia
widget:
- text: a photo of HFHKDaphnia Anomopoda in the Acropolis
---

# DreamBooth model for the HFHKDaphnia concept trained by misza222 on the misza222/dreambooth-hackathon-Daphnia dataset.

This is a Stable Diffusion model fine-tuned on the HFHKDaphnia concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of HFHKDaphnia Anomopoda**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `Anomopoda` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('misza222/HFHKDaphnia-Anomopoda-lr1e-06-max_train_steps1200')
image = pipeline().images[0]
image
```
