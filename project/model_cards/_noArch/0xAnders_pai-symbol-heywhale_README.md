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
- text: A photo of a pai symbol
---

# DreamBooth model for the pai concept trained by 0xAnders.

This is a Stable Diffusion model fine-tuned on the pai concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of pai symbol**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `symbol` images for the science theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('0xAnders/pai-symbol-heywhale')
image = pipeline().images[0]
image
```

## Examples

**a photo of pai symbol in the Great Wall↓**
![](https://www.hualigs.cn/image/63c97770bc2d4.jpg)

![](https://www.hualigs.cn/image/63c976a57c21f.jpg)
