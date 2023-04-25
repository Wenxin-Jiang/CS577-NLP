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
- text: Fallout concept of fforiver river in front of the Great Pyramid of Giza
---

# DreamBooth model for the fforiver concept trained on the CCMat/forest-river dataset.

This is a Stable Diffusion model fine-tuned on the fforiver concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of fforiver river**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `river` images for the landscape theme.

Pretrained Model: prompthero/openjourney



## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('CCMat/fforiver-river-mdj')
image = pipeline().images[0]
image
```

## Samples

Prompt: "high quality photo of fforiver river along the Colosseum in Rome"
![example images](images/0f47ccb9e7fb4e8c9fff7733351fc79c.png)
<br>

Prompt: "Fallout concept of fforiver river in front of Chichén Itzá in Mexico, sun rays, unreal engine 5"
![example images](images/07d8d8f43d1d184b5e3fc62bb3efddd6.png)
<br>
