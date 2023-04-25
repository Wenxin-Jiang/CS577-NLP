---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- food
widget:
- text: a photo of a field of tortas
---

# DreamBooth model for the torta concept trained by morgan on the morgan/tortas dataset.

This is a Stable Diffusion model fine-tuned on the torta concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of a torta sandwich**

See the ongoing experiments here in this [Weights & Biases training journal](https://wandb.ai/morgan/hf-dreambooth/reports/Training-Journal-DreamBooth-fine-tuning--VmlldzozMjA4MzE4#jan-1,-11:50---try-add-%22sandwich%22-class-to-the-training-prompt---success!)

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

Note that commit `8f89857b2b2a6f75c443eac298f022483ef23a3f` uses the concept name `zztortazz` instead of `torta`, to see if this more unique concept name works better (spoiler, it doesn't)

## Description


This is a Stable Diffusion model fine-tuned on images of tortas.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('morgan/torta')
image = pipeline().images[0]
image
```
