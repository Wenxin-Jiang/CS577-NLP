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
- text: a photo of cute hhog hedgehog eating cookies
---

# DreamBooth model for the astronomy concept trained by Dhruv Singal on a dataset of hedgehog images from Kaggle[link](https://www.kaggle.com/datasets/therealoise/hedgehogs-and-porcupines).

This is a Stable Diffusion 2.1 model fine-tuned on the hedgehog concept with DreamBooth. It can be used by modifying the `instance_prompt`: a photo of cute hhog hedgehog eating cookies****

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Example
![](download.png)
## Description


This is a Stable Diffusion model fine-tuned on images of cute hedgehogs.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('alphatozeta/hhog-hedgehog')
image = pipeline().images[0]
image
```
