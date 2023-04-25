---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Model Card for Stable Diffusion - Pokemon, 256px
Model developed for the Unit 1 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class).

This model is a diffusion model for unconditional image generation of Pokemon [![PikachuCool](https://cdn3.emoji.gg/emojis/5085-pikachucool.png)](https://emoji.gg/emoji/5085-pikachucool)  
It is trained on a small collection of pokemon pictures and trained for 50 epochs, with 🤗 Accelerate.

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('alkiskoudounas/sd-pokemon-256px')

```

## Example
Here you can find an example of the output of the model, in a batch of 8 images:

![Pokemon Example](pokemon-256px-examples.png)

