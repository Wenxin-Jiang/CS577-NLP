---
language: 
  - en
thumbnail: TBD
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
datasets:
- ChristophSchuhmann/improved_aesthetics_6plus
---


# Mini Stable Diffusion (miniSD)

MiniSD is a latent text-to-image diffusion model that has been conditionned on 256x256 images through finetuning.

## Examples

WIP

## Usage

```
!pip install diffusers==0.3.0
!pip install transformers scipy ftfy
```

```
import torch
from diffusers import StableDiffusionPipeline
from torch import autocast

# TODO: change model_id to "lambdalabs/miniSD"
pipe = StableDiffusionPipeline.from_pretrained("eolecvk/model-test", torch_dtype=torch.float16)  
pipe = pipe.to("cuda")

prompt = "Yoda"
scale = 10
n_samples = 4

# Sometimes the nsfw checker is confused, you can disable it at your own risk here
disable_safety = False

if disable_safety:
  def null_safety(images, **kwargs):
      return images, False
  pipe.safety_checker = null_safety

with autocast("cuda"):
  images = pipe(n_samples*[prompt], guidance_scale=scale).images

for idx, im in enumerate(images):
  im.save(f"{idx:06}.png")
```

