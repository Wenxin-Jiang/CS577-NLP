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
- text: a photo of flufflemarkednoser cat in the bookstore
---

# DreamBooth model for the flufflemarkednoser concept trained by Nlpeva on the Nlpeva/Calico_fluffy dataset.

This is a Stable Diffusion model fine-tuned on the flufflemarkednoser concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of flufflemarkednoser cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `cat` images for the animal theme. It is based on ten images of a calico cat. It works well for phrases like on the moon and at the beach. The cat, Sharpie, was called that because of her distinctive black nose that looks like someone drew on it with a permanent marker.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Nlpeva/flufflemarkednoser-cat')
image = pipeline().images[0]
image
```
