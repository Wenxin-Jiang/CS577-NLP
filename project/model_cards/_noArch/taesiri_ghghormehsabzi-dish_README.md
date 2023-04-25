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
widget:
- text: a photo of ghghormehsabzi dish in an italian resturant
---

# DreamBooth model for the ghghormehsabzi concept trained by taesiri on the dataset.

This is a Stable Diffusion model fine-tuned on the ghghormehsabzi concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of ghghormehsabzi dish**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `Ghormeh Sabzi` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('taesiri/ghghormehsabzi-dish')
image = pipeline().images[0]
image
```

## Sample images

![sample resultsa](sample-image.png)
