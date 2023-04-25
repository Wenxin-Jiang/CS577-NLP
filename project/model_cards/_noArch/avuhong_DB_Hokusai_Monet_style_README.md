---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- landscape
- classical-art
widget:
- text: a painting in $M## style of a fishing village under a cherry blossom forest at sunset
---

# DreamBooth model for the painting of mixed style between Claude-Monet and Hokusai

This is a Stable Diffusion model fine-tuned to generate mixed styled paintings between Claude-Monet and Hokusai taught to Stable Diffusion with DreamBooth.
It can be used by modifying the `instance_prompt`: **a painting in $M## style of**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on paintings of both Claude-Monet and Hokusai.

## Examples

Since it's more for landscape painting, the image size matters. I found that 512*1024 normally gave interesting results.
Check out this gallery for more generated images:
https://www.vuhongai.com/classicalart-ai

## Usage
```python
from diffusers import StableDiffusionPipeline
pipeline = StableDiffusionPipeline.from_pretrained('avuhong/DB_Hokusai_Monet_style')
prompt = "a painting in $M## style of a fishing village under a cherry blossom forest at sunset"
image = pipe(prompt, 
             num_inference_steps=200, 
             guidance_scale=5, 
             height=512, width=1024,
            ).images[0]
image
```