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
- text: a photo of coco cat wearing awesome glasses in a forest full of sunshine
---

# DreamBooth model for the coco concept trained by avocadogogo.

This is a Stable Diffusion model fine-tuned on the coco concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of coco cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `cat` images for the animal theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('avocadogogo/coco-cat-heywhale')
image = pipeline().images[0]
image
```
## cases（prompt）
a photo of coco cat sitting on top of the deck of a battle ship traveling through the open sea with a lot of ships surrounding it
![WechatIMG526.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1673934393994-636a6cd1bb644b7ee63bbaf7.jpeg)
a photo of coco cat wearing awesome glasses in a forest full of sunshine
![WechatIMG527.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1673934394003-636a6cd1bb644b7ee63bbaf7.jpeg)
a cartoon digital art of coco cat
![index.jpg](https://s3.amazonaws.com/moonup/production/uploads/1673938250984-636a6cd1bb644b7ee63bbaf7.jpeg)
![index2.jpg](https://s3.amazonaws.com/moonup/production/uploads/1673938250986-636a6cd1bb644b7ee63bbaf7.jpeg)
