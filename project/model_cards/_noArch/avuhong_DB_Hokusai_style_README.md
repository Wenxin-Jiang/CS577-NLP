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

# DreamBooth model for the painting of Hokusai style

This is a Stable Diffusion model fine-tuned Hokusai's painting style taught to Stable Diffusion with DreamBooth.
It can be used by modifying the `instance_prompt`: **a painting in $M## style of**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on Hokusai's paintings, a Japanese artist from the Edo period (1760-1849). The AI model used to create these works was primarily trained on Hokusai's most famous series of woodblock prints, called the Thirty-Six Views of Mount Fuji including the iconic The Great Wave off Kanagawa.

## Examples

Since it's more for landscape painting, the image size matters. I found that 512*1024 normally gave interesting results.
Check out this gallery for more generated images:
https://www.vuhongai.com/classicalart-ai

## Usage

```python
from diffusers import StableDiffusionPipeline
pipeline = StableDiffusionPipeline.from_pretrained('avuhong/DB_Hokusai_style')

prompt = "a painting in $M## style of a fishing village under a cherry blossom forest at sunset"
image = pipe(prompt, 
             num_inference_steps=200, 
             guidance_scale=5, 
             height=512, width=1024,
            ).images[0]
image
```