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
widget:
- text: clashgoblin person Portrait, by Jakub Rozalski.
---

# DreamBooth model for the clashgoblin concept trained by GV05 on the GV05/dreambooth-hackathon-images dataset.

This is a Stable Diffusion model fine-tuned on the clashgoblin concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of clashgoblin person**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Images generated by model

![Image alt text](result.png)


## Description


This is a Stable Diffusion model fine-tuned on goblin charachter images from clash royale game for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline
prompt = "clashgoblin person Portrait, by Jakub Rozalski."
pipeline = StableDiffusionPipeline.from_pretrained('GV05/clashgoblin-person')
image = pipeline(prompt, guidance_scale=9).images[0]
image
```
