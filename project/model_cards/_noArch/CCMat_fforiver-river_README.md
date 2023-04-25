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
widget:
- text: professional photo of fforiver river running alongside the Colosseum in Rome
---

# DreamBooth model for the fforiver concept trained on the CCMat/forest-river dataset.

This is a Stable Diffusion model fine-tuned on the fforiver concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of fforiver river**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `river` images for the landscape theme.

Pretrained Model: nitrosocke/elden-ring-diffusion



## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('CCMat/fforiver-river')
image = pipeline().images[0]
image
```

## Samples

Prompt: "fforiver river in front of the The Taj Mahal, professional photograph"
![example images](images/3a785d0e5c6530d9cfdb3f073d1722e0.png)
<br>

Prompt: "Fallout concept of fforiver river in front of Chichén Itzá in Mexico, sun rays, unreal engine 5"
![example images](images/0c9a1d383061e3d503ce76a81d59ad0d.png)
<br>

Prompt: "high quality photo of fforiver river along the Colosseum in Rome"
![example images](images/52f0da962a364062d8c485a30343d7c4.png)
<br>

Prompt: "Oil painting of fforiver river in front of the Machu Picchu"
![example images](images/85d4eeb7c7374aa20a08806046ed5ee7.png)
<br>
