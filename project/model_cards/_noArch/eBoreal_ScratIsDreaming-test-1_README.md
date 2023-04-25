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
- text: scrrrsc squirrel  sleeping in a bath full of acorn nuts, pixar style, bokeh
---

# DreamBooth model for the scrrrsc concept trained by eBoreal on the eBoreal/scrat-imgs dataset.

This is a Stable Diffusion model fine-tuned on the scrrrsc concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of scrrrsc squirrel**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


Quiet, Scrat is dreaming !
Ps: This is a Stable Diffusion model fine-tuned on `squirrel` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('eBoreal/ScratIsDreaming-test-1')
image = pipeline().images[0]
image
```
