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
- text: a itgted air jordan 1,((side view)),colourful,optimized structure,Product
    photography,realistic details,complete single object in the centere,HD
---

# DreamBooth model for the itgted concept trained by Yuheng111.

This is a Stable Diffusion model fine-tuned on the itgted concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of itgted slipper**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a sneaker design auxiliary model trained on a stable diffusion model, Combining the traditional form of sneakers with the integration and layered features of 3D printing，
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Yuheng111/3d-print-style-snkr-gererate')
image = pipeline().images[0]
image
```
