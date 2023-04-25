---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- food
datasets: Ashish08/vada-sambhar
widget:
- text: a photo of vada sambhar south indian dish on a red table
---

# DreamBooth model for the vada-sambhar concept trained by Ashish08 on the Ashish08/vada-sambhar dataset.

This is a Stable Diffusion model fine-tuned on the vada-sambhar concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of vada-sambhar south-indian-dish**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `south-indian-dish` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Ashish08/vada-sambhar-south-indian-dish')
image = pipeline().images[0]
image
```
