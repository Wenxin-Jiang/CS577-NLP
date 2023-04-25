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
- text: a photo of ancma map of beautiful flower garden.
---

## Description
This is a Stable Diffusion model fine-tuned on a 100 ancient/old maps for the DreamBooth Hackathon 🔥 wildcard theme. To participate or learn more, visit [this page](https://huggingface.co/dreambooth-hackathon). 

To generate ancient/old maps, use **a photo of ancma map of [your choice]**. Modifiers and negative prompts may improve results. The model is not limited to classic geography, you can try gardens, cave systems, cities, planets, zodiac charts, etc.

## Examples
*a photo of ancma map of fiery volcano island.*
![volcano map](https://i.imgur.com/OTmNUx8.png)
*a photo of ancma map of peaceful Swiss town near a lake.*
![swiss map](https://i.imgur.com/7FJRab8.png)
*a photo of ancma map of giant ant colony.*
![ant map](https://i.imgur.com/zsez6Of.png)
*a photo of ancma map of beautiful flower garden.*
![garden map](https://i.imgur.com/WKlN4PL.png)


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('baruga/ancient-maps')
image = pipeline().images[0]
image
```
