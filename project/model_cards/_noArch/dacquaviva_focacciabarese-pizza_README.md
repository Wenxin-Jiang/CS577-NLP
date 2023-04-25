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
  - text: focacciabarese pizza with a nice sea view.
---

# DreamBooth model for the focacciabarese concept trained by dacquaviva on the dacquaviva/focacciabarese dataset.

This is a Stable Diffusion model fine-tuned on the focacciabarese concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of facacciabarese pizza**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on my `pizza` images for the food theme. In Bari (Puglia south of Italy), the focaccia is a kind of bread, seasoned with tomatoes, olives, virgin olive oil, and oregano. It is made with poor, very simple, and local ingredients. :).
                    
## Usage

```python
from diffusers import StableDiffusionPipeline
pipeline = StableDiffusionPipeline.from_pretrained('dacquaviva/focacciabarese-pizza')
image = pipeline().images[0]
image
```
        