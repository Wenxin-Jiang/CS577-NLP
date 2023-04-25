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
- text: a photo of bongodog dog in the Acropolis
---

# DreamBooth model for the bongodog concept trained by dacquaviva on the dacquaviva/bongodog dataset.

This is a Stable Diffusion model fine-tuned on the bongodog concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of bongodog dog**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on my `dog` images for the animal theme. His name is Bongo :).

## Photo of my dog Bongo:
<img src="https://drive.google.com/uc?export=view&id=1m5heLYYzQIxDeyNoxxtB6X7bwNhxqG9v" alt="bongodog" width="200"/>
<img src="https://drive.google.com/uc?export=view&id=1nP3JqAYEZSlTFAgduhhFC6S7XYKo8Nz9" alt="bongodog" width="200"/>

## Examples of generated images:
<img src="https://drive.google.com/uc?export=view&id=1DaJUXJP2nQy0_TVQpf3QAaJd6rBfbOlo" alt="bongodog" width="200"/>
<img src="https://drive.google.com/uc?export=view&id=1ybeN5vg0OYuSalOenQX8AB8yaYBRW3O0" alt="bongodog" width="200"/>
<img src="https://drive.google.com/uc?export=view&id=1-HqsSQpuPIh8Y8C0kD92mPs_Rd68cPik" alt="bongodog" width="200"/>
<img src="https://drive.google.com/uc?export=view&id=1JvUDQuTC0oaZiFPKQXUfUsHfhr8LLpCw" alt="bongodog" width="200"/>

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('dacquaviva/bongodog-dog')
image = pipeline().images[0]
image
```