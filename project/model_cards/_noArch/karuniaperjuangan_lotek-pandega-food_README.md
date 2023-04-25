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
- text: 3d render of lotek pandega food, vray, ray tracing, hyperrealistic,octane
    render
---

# DreamBooth model for the lotek pandega concept trained by karuniaperjuangan on a custom dataset.

This is a Stable Diffusion model fine-tuned on the lotek pandega concept with DreamBooth. It can be used by modifying the `instance_prompt`: **lotek pandega food**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on `lotek pandega food` images for the food theme.

## Examples
| 3d render of lotek pandega food, vray, ray tracing, hyperrealistic,octane render | anime illustration of lotek pandega food, by studio ghibli, cartoon illustration | comic illustration of lotek pandega food, marvel comic cover, by stan lee |
| -- | -- | -- |
| ![](image_sample/1.png) | ![](image_sample/2.png) | ![](image_sample/3.png) |

| illustration of a young handsome man holding fork and eating lotek pandega food, art by greg rutkowski, ilya kushinov | portrait of cristiano ronaldo eating lotek pandega food, intricate handsome cr7 face | sketch drawing of lotek pandega food, pencil drawing by Paul Cadden |
| -- | -- | -- |
| ![](image_sample/4.png) | ![](image_sample/5.png) | ![](image_sample/6.png) |

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('karuniaperjuangan/lotek-pandega-food')
image = pipeline().images[0]
image
```
