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
datasets: misza222/dreambooth-hackathon-owczarek
widget:
- text: a photo of OwczarekPodhalanski dog in the Acropolis
---

# DreamBooth model for the OwczarekPodhalanski concept trained by misza222 on the misza222/dreambooth-hackathon-owczarek dataset.

This is a Stable Diffusion model fine-tuned on the OwczarekPodhalanski concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of OwczarekPodhalanski dog**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `dog` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('misza222/OwczarekPodhalanski-dog-lr1e-06-max_train_steps1200')
image = pipeline().images[0]
image
```
