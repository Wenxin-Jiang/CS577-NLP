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
- text: a photo of a jaffa cake
---

# DreamBooth model for the jaffa concept trained by dogeplusplus on some images of jaffa cakes.

This is a Stable Diffusion model fine-tuned on the jaffa concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of a jaffa cake**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

| Stable Diffusion v1-4 | Dreambooth Jaffa |
| -- | -- |
|  ![](stable-jaffa.png) | ![](dreambooth-jaffa.png) |

Generate images of jaffa cakes in different contexts and art styles:

| ukiyo-e | picasso | rembrandt |
| -- | -- | -- |
| ![](ukiyoe-jaffa.png) | ![](picasso-jaffa.png) | ![](rembrandt-jaffa.png) |
| **van gogh** | **warhol** | **dali** |
| ![](vangogh-jaffa.png) | ![](warhol-jaffa.png) | ![](dali-jaffa.png) |

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('dogeplusplus/jaffa-cake')
image = pipeline().images[0]
image
```
