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


This is a Stable Diffusion model fine-tuned on `llama` images for the animal theme.

### Training Hyperparemeters

Pretrained Model: [stabilityai/stable-diffusion-2](https://huggingface.co/stabilityai/stable-diffusion-2)<br>
Learning rate: 1e-6<br>
Steps:1100<br>




## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('CCMat/fluffalpaca-llama-1100')
image = pipeline().images[0]
image
```

## Samples

Prompt: "fluffalpaca llama in space by Enki Bilal"
![example images](images/7628798d62fe75777a9dc58d88fabd54.png)


Prompt: "fluffalpaca llama in front of the Eiffel Tower"
![example images](images/19a272275e0297b8c7772532f29ec5a1.png)


Prompt: "a photo of fluffalpaca llama swimming in the river"
![example images](images/dc86f23f335f9105e5761c407eb523aa.png)


Prompt: "a photo of fluffalpaca llama in front of the Colosseum in Rome, professional photograph"
![example images](images/f0b473cae57124bc3551a5f65bef3511.png)


Prompt: "USSR propoganda poster. Long live the fluffalpaca llama"
![example images](images/ef7ee593768a5917268b5434985ae4be.png)
