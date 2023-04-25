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
- text: ctm curry dish in a rustic modern farmhouse kitchen
---

# DreamBooth model for the ctm concept trained by jnick on the jnick/chicken-tikka-masala dataset.

This is a Stable Diffusion model fine-tuned on the ctm concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of ctm curry dish**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on images of chicken tikka masala for the food theme. Here are some examples:

| "an adorable puppy sniffing ctm curry dish" | "ctm curry dish  in the style of Johannes Vermeer" |
| -- | -- |
| ![](chicken-tikka-masala-1.png) | ![](chicken-tikka-masala-2.png) |

| "a delicious plate of ctm curry dish in the Grand Canyon" | "ctm curry dish  in a modern science laboratory" |
| -- | -- |
| ![](chicken-tikka-masala-3.png) | ![](chicken-tikka-masala-4.png) |

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('jnick/chicken-tikka-masala')
image = pipeline().images[0]
image
```
