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
- text: a picture of spaeti store in the forest
datasets:
- malysheva42/spaeti_store
language:
- en
---

# DreamBooth model for the spaeti concept trained by malysheva42 on the malysheva42/spaeti_store dataset.

This is a Stable Diffusion model fine-tuned on the spaeti (späti) concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of spaeti store**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `store` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('malysheva42/spaeti_store_2')
image = pipeline().images[0]
image
```

## Examples
1. a picture of spaeti store in the forest
![a picture of spaeti store in the forest](sample-image-forest.png)

2. a picture of spaeti store on the beach near the sea, best quality
![a picture of spaeti store on the beach near the sea, best quality](sample-image-beach.png)

3. a picture of spaeti store in the snow
![a picture of spaeti store in the snow](sample-image-snow.png)