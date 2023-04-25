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
- text: a photo of fluffalpaca llama in front of the Colosseum in Rome
---

# DreamBooth model for the fluffalpaca concept trained on the CCMat/db-aplaca dataset.

This is a Stable Diffusion model fine-tuned on the fluffalpaca concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of fluffalpaca llama**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `llama` images for the animal theme.<br>

### Training Hyperparemeters

Pretrained Model: [stabilityai/stable-diffusion-2](https://huggingface.co/stabilityai/stable-diffusion-2)<br>
Learning rate: 1e-6<br>
Steps:1078<br>



## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('CCMat/fluffalpaca-llama-1078')
image = pipeline().images[0]
image
```
