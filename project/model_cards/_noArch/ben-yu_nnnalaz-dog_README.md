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
- text: Cute and adorable cartoon fluffy nnnalaz dog with a scarf, fantasy, dreamlike,
    city scenario, surrealism, super cute, trending on artstation
---

# DreamBooth model for the nnnalaz concept trained by ben-yu on the ben-yu/dreambooth-hackathon-nala dataset.

This is a Stable Diffusion model fine-tuned on the nnnalaz concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of nnnalaz dog**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `dog` images for the animal theme.

Prompt: `Cute and adorable cartoon fluffy nnnalaz dog with a scarf, fantasy, dreamlike, city scenario, surrealism, super cute, trending on artstation`

![](cute.png)

Prompt: `Portrait painting of a cute nnnalaz dog with armor, ultra realistic, concept art, intricate details, eerie, highly detailed, photorealistic, octane render, 8 k, unreal engine. art by artgerm and greg rutkowski and charlie bowater and magali villeneuve and alphonse mucha`

![](armour.png)

Prompt: `portrait of nnnalaz husky anthro as a astronaut, retro futurism, art deco, detailed, painterly digital art by wlop and cory loftis and delphin enjolras, 🐿🍸🍋, furaffinity, trending on artstation`
![](astro_2.png)
![](astro.png)



## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('ben-yu/nnnalaz-dog')
image = pipeline().images[0]
image
```
