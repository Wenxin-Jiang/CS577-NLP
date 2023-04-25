---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- wildcard
widget:
- text: a photorealistic image of srkay
---

# DreamBooth model for the srkay concept trained by Xhaheen on the Xhaheen/dreambooth-hackathon-images-srkman-2 dataset.

This is a Stable Diffusion model fine-tuned on the sha rukh khan images  with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of srkay man**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!
## Dataset used

![srkmansd (17).png](https://s3.amazonaws.com/moonup/production/uploads/1673107436292-621c88aca7d6c7e0563256ae.png)
![srkmansd (18).png](https://s3.amazonaws.com/moonup/production/uploads/1673107436124-621c88aca7d6c7e0563256ae.png)
 
![srkmansd (16).png](https://s3.amazonaws.com/moonup/production/uploads/1673107436048-621c88aca7d6c7e0563256ae.png)
## Description


This is a Stable Diffusion model fine-tuned on `man` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Xhaheen/srkay-man_6-1-2022')
image = pipeline().images[0]
image
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1FmTaUN38enNdCgi4HxG0LMZ4HobM0Iq3?usp=sharing)


