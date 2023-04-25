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
- text: "a photo of a duckduck roast_duck walking in the water"
  example_title: photo
- text: "A painting of of a duckduck roast_duck wearing a suit, natural light, in the sky, with bright colors, by Studio Ghibli"
  example_title: painting
- text: "a pov google earth satellite photo of a duckduck roast_duck running,by the vaporwave pool,cinematic lighting , macro lens, iphone x,by enki bilal,highly detailed, HDR, UHD, 64K"
  example_title: satellite photo
---

# DreamBooth model for the duckduck concept trained by shadow.

This is a Stable Diffusion model fine-tuned on the duckduck concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of duckduck roast_duck**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `roast_duck` images for the food theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.

![roast_duck](cf755105-7db6-4220-9779-b37db63b2b52.jpeg "roast_duck")
![roast_duck](20230114223341.png "roast_duck")
![roast_duck](20230112094210.png "roast_duck")
![roast_duck](20230112093456.png "roast_duck")
![satellite roast_duck](ca475558-84c8-4234-ba04-9bad2b400124.jpeg "roast_duck")

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('shadow/duckduck-roast_duck-heywhale')
image = pipeline().images[0]
image
```
