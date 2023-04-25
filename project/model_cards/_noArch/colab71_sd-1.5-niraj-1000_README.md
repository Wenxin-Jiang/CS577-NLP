---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- man
widget:
- text: photo of ukj
---
# Settings
Steps:1000

Class Images:50

# DreamBooth model for the niraj concept trained by colab71 on the  dataset.

This is a Stable Diffusion model fine-tuned on the niraj concept with DreamBooth. It can be used by modifying the 

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on niraj's images for the person theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('colab71/sd-1.5-niraj-1000')
image = pipeline().images[0]
image
```
