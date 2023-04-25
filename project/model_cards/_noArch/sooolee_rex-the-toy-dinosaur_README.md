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
datasets: sooolee/rexthetoy
widget:
- text: a photo of rxty dinosaur reading a book in a cafe
---

# DreamBooth model for the rxty concept trained by sooolee on the sooolee/rexthetoy dataset.

This is a Stable Diffusion model fine-tuned on the rxty concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of rxty dinosaur**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on `dinosaur` images for the wildcard theme. The model was trained with a learning rate of `1e-06` and `1000` train steps.

## Some Output Examples

Inferences were made with a guidance scale between 8 - 11 and inference steps of 300 - 400. 

#### In Various Places
![in_places](https://huggingface.co/sooolee/rex-the-toy-dinosaur/resolve/main/in_places.png)

#### In the Style of Various Artists
![artistic_rendering](https://huggingface.co/sooolee/rex-the-toy-dinosaur/resolve/main/artistic_rendering.png)

#### Doing Things
![doing_things](https://huggingface.co/sooolee/rex-the-toy-dinosaur/resolve/main/doing_things.png)


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('sooolee/rex-the-toy-dinosaur')
image = pipeline().images[0]
image
```
