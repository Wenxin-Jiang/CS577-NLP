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
- text: a photo of blofi fish in Times Square.
---

## Description
This is a Stable Diffusion model fine-tuned on the infamous blobfish (often remarked as the ugliest animal in the world) for the DreamBooth Hackathon 🔥 animal theme. To participate or learn more, visit [this page](https://huggingface.co/dreambooth-hackathon). 

To generate blobfish images, use **a photo of blofi fish in [your choice]** or experiment with other variations. For some reason, GFC scale 5 seems to give the best results, at 7 images start get "overcooked". Despite multiple training runs with various settings, I couldn't fully solve this problem. Additional modifiers and negative prompts may also improve results.

## Examples
*a photo of blofi fish wearing a beautiful flower crown.*
![flower blobfish](https://i.imgur.com/at5N7Qd.png)
*a photo of blofi fish in nerdy glasses.*
![jungle fractal](https://i.imgur.com/pZt8uSn.png)
*a photo of blofi fish at the Arctic in a fluffy hat.*
![arctic blobfish](https://i.imgur.com/ttVmZbM.png)
*top rated surrealist painting of blofi fish by Salvador Dalí, intricate details.*
![painting blobfish](https://i.imgur.com/ufQfufU.png)
*top rated colorful origami photo of blofi fish.*
![origami blobfish](https://i.imgur.com/SgkffkV.png)


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('baruga/hideous-blobfish')
image = pipeline().images[0]
image
```
