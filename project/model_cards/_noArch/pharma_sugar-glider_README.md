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
- text: a photo of a pssg wearing goggles
- text: a photo of a pssg sugar glider wearing goggles
---

# DreamBooth model for the pssg concept trained by pharmapsychotic

**Sugar gliders** are adorable creatures! I've never had one as a pet but I've been tempted. Imagine having one in your shirt pocket and feeding it snacks as you work. 😍

Anyway, I created a few AI renders of sugar gliders and mixed in with some photos of the critters and trained a model for the [DreamBooth Hackathon](https://huggingface.co/dreambooth-hackathon)! If you enjoy the model or just find the results funny and cute, drop a like on the model!

To use the model be sure to include `pssg` in your prompt (PharmapSychotic Sugar Glider) or `pssg sugar glider` for a stronger effect. I recommend using a version of the inference that has cross attention control so you can balance the influence of the sugar glider and the weird scenarios you put him in. I trained to 10,000 steps and it overcooked so dropped back to the 2,500 step checkpoint but still need to boost other things in the prompts like `(((goggles)))` to overcome the default `pssg` influence.

See below for usage!


## Examples

|                           |                            |                              |
| ------------------------- | -------------------------- | ---------------------------- |
| ![](examples/dj.png)      | ![](examples/fantasy1.png) | ![](examples/fantasy2.png)   |
| ![](examples/glasses.png) | ![](examples/goggles.png)  | ![](examples/red_carpet.png) |
| ![](examples/robo.png)    | ![](examples/tron.png)     | ![](examples/bitcoin.png)    |


## Usage

#### With Diffusers

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('pharma/sugar-glider')
image = pipeline().images[0]
image
```

#### With SD Web UI
To use with SD Web UI download [sugar_gliders_pssg_2500.ckpt](https://huggingface.co/pharma/sugar-glider/resolve/main/sugar_gliders_pssg_2500.ckpt) and put in your models folder.