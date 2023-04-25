---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- dreambooth-hackathon
- cat
widget:
- text: vishu
---

## Description


Model finetuned on the pictures of our cat named Vishu, made for the Dreambooth Hackathon


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Apocalypse-19/dreambooth-vishu')
image = pipeline().images[0]
image
```
