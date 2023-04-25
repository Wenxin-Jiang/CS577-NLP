---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- science
widget:
- text: A painting of StarTrek starship, Michelangelo style
---

# DreamBooth model for the StarTrek concept trained by vumichien on the vumichien/spaceship_star_trek dataset.

<img src="https://huggingface.co/vumichien/StarTrek-starship/resolve/main/1_dlgd3k5ZecT17cJOrg2NdA.jpeg" alt="StarTrek starship">

This is a Stable Diffusion model fine-tuned on the StarTrek concept with DreamBooth. It can be used by modifying the `instance_prompt`: **StarTrek starship**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `starship` images for the science theme.

## Examples

<figure>
  <img src="https://huggingface.co/vumichien/StarTrek-starship/resolve/main/Leonardo%20Da%20Vinci%20style.png" alt="StarTrek starship - Leonardo Da Vinci style">
  <figcaption>Text prompts for generated: A painting of StarTrek starship, Leonardo Da Vinci style
  </figcaption>
</figure>

<figure>
  <img src="https://huggingface.co/vumichien/StarTrek-starship/resolve/main/Michelangelo%20style.png" alt="StarTrek starship - Michelangelo style">
  <figcaption>Text prompts for generated: A painting of StarTrek starship, Michelangelo style
  </figcaption>
</figure>

<figure>
  <img src="https://huggingface.co/vumichien/StarTrek-starship/resolve/main/Botero%20style.png" alt="StarTrek starship - Botero style">
  <figcaption>Text prompts for generated: A painting of StarTrek starship, Botero style
  </figcaption>
</figure>

<figure>
  <img src="https://huggingface.co/vumichien/StarTrek-starship/resolve/main/Pierre-Auguste%20Renoir%20style.png" alt="StarTrek starship - Pierre-Auguste Renoir style">
  <figcaption>Text prompts for generated: A painting of StarTrek starship, Pierre-Auguste Renoir style
  </figcaption>
</figure>

<figure>
  <img src="https://huggingface.co/vumichien/StarTrek-starship/resolve/main/Vincent%20Van%20Gogh%20style.png" alt="StarTrek starship - Vincent Van Gogh style">
  <figcaption>Text prompts for generated: A painting of StarTrek starship, Vincent Van Gogh style
  </figcaption>
</figure>

<figure>
  <img src="https://huggingface.co/vumichien/StarTrek-starship/resolve/main/Rembrandt%20style.png" alt="StarTrek starship - Rembrandt style">
  <figcaption>Text prompts for generated: A painting of StarTrek starship, Rembrandt style
  </figcaption>
</figure>

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('vumichien/StarTrek-starship')
image = pipeline().images[0]
image
```
