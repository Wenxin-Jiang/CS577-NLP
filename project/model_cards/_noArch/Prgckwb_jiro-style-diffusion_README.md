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
- text: a photo of jirostyle ramen noodles in the park
---

# DreamBooth model for the jirostyle concept trained by Prgckwb on the Prgckwb/jiro-style-ramen dataset.

This is a Stable Diffusion model fine-tuned on the jirostyle concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of jirostyle ramen noodles**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `ramen noodles` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Prgckwb/JiroStyle-ramen')
prompt = "a photo of jirostyle ramen noodles"

image = pipeline(prompt).images[0]
```

## Generated Images
**a watercolor painting of jirostyle ramen noodles**
![](a_watercolor_painting_of_jirostyle_ramen_noodles.png)

**a photo of a dog eating jirostyle ramen noodles in the park**
![](a_photo_of_a_dog_eating_jirostyle_ramen_noodles_in_the_park.png)

**a photo of jirostyle ramen noodles on the table**
![](a_photo_of_jirostyle_ramen_noodles_on_the_table.png)
