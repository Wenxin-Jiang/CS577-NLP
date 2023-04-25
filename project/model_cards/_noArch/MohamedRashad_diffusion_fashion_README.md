---
language: en
tags:
- stable-diffusion
- diffusers
- text-to-image
- fashion
- diffusion
- openjourney
inference: true
license: openrail
library_name: diffusers
---

# Stable Diffusion fine-tuned for [Fashion Product Images Dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset) 

This model is a fine-tuned version of [openjourney](https://huggingface.co/prompthero/openjourney) that is based on Stable Diffusion targeting fashion and clothing.

## How to use ?

```python
from diffusers import StableDiffusionPipeline
import torch

pipeline = StableDiffusionPipeline.from_pretrained("MohamedRashad/diffusion_fashion", torch_dtype=torch.float16)
pipeline.to("cuda")

prompt = "A photo of a dress, made in 2019, color is Red, Casual usage, Women's cloth, something for the summer season, on white background"
images = pipeline(prompt).images[0]
image.save("red_dress.png")

```

## Any feedback or questions are welcomed on the [community](https://huggingface.co/MohamedRashad/diffusion_fashion/discussions) tab