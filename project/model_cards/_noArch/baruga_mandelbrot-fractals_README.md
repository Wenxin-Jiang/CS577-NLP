---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- science
widget:
- text: top rated photo of mafra fractal in the shape of seashells.
---

## Description
This is a Stable Diffusion model fine-tuned on Mandelbrot fractal images for the DreamBooth Hackathon 🔥 science theme. To participate or learn more, visit [this page](https://huggingface.co/dreambooth-hackathon). 

To generate Mandelbrot fractals, use **a photo of mafra fractal in the shape of [your choice]** or experiment with other variations. CFG scale seems to be the best around 8-9. Additional modifiers and negative prompts may also improve results.

## Examples
*a photo of mafra fractal in the shape of a squid.*
![squid fractal](https://i.imgur.com/UHJ5K7J.png)
*a photo of mafra fractal in the shape of seashells.*
![seashell fractal](https://i.imgur.com/PgzEOAV.png)
*a photo of mafra fractal in the shape of jungle foliage.*
![jungle fractal](https://i.imgur.com/v6ISc3u.png)
*a photo of mafra fractal in the shape of a beautiful flower.*
![flower fractal](https://i.imgur.com/9VIk2Jc.png)


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('baruga/mandelbrot-fractals')
image = pipeline().images[0]
image
```
