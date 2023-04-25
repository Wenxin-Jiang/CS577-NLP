---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- animal
widget:
- text: a photo of shoebill bird as a gold monument in the Alhambra Granada Spain, realistic, camera, 35mm
---

# DreamBooth model for the shoebill concept trained by fnavales

This is a Stable Diffusion model fine-tuned on the shoebill concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of shoebill bird**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `bird` images for the animal theme.

The shoebill, also known as the shoebill stork or Balaeniceps rex, is a large bird native to swamps in East Africa. 
It is known for its distinctive appearance, with a long, narrow bill that resembles a shoe and a tall, thick neck. 
It has a mostly grey plumage, with a white belly and a few patches of brown and black on its wings and back.

The shoebill is a carnivorous bird, and it feeds mainly on fish, although it has also been known to eat reptiles, mammals, and birds. 
It is a solitary and elusive bird, and it is not commonly seen in the wild. 
The shoebill is endangered, and it is protected by law in many of the countries where it is found.

## Examples

|                  |                   | 
| ---------------- | ----------------- | 
| ![](ex1.jfif)    | ![](ex3.jfif)     | 
| ![](ex2.jfif)    | ![](ex4.png)     | 

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('fnavales/shoebill-bird-fnavales')
image = pipeline().images[0]
image
```
