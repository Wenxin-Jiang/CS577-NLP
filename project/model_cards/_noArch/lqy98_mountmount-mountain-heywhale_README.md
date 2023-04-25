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
- text: Streams crossing the mountmount in a sunny day
---

# DreamBooth model for the mountmount concept trained by lqy98.

This is a Stable Diffusion model fine-tuned on the mountmount concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of mountmount mountain**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

Concept Image
![1.png](1.png)

Output Imgae
![2.png](2.png)

## Description

This is a Stable Diffusion model fine-tuned on `mountain` images for the landscape theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('lqy98/mountmount-mountain-heywhale')
image = pipeline().images[0]
image
```
