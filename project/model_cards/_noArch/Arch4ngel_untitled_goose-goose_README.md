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
datasets: Arch4ngel/untitled_goose_game
widget:
- text: untitled_goose goose on an airplane
---

# DreamBooth model for the untitled_goose concept trained by Arch4ngel on the Arch4ngel/untitled_goose_game dataset.

This is a Stable Diffusion model fine-tuned on the untitled_goose concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of untitled_goose goose**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


Stable Diffusion model fine-tuned for generating Goose from Untitled Goose Game images.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Arch4ngel/untitled_goose-goose')
image = pipeline().images[0]
image
```
