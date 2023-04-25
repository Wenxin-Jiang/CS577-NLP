---
language: 
  - en
thumbnail: "https://s3.amazonaws.com/moonup/production/uploads/1663756797814-62bd5f951e22ec84279820e8.png"
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
datasets:
- eolecvk/naruto-blip-captions
---


# Naruto diffusers (new version available [here](https://huggingface.co/lambdalabs/sd-naruto-diffusers))

__Stable Diffusion fine tuned on Naruto by [Lambda Labs](https://lambdalabs.com/).__

Put in a text prompt and generate your own Naruto character, no "prompt engineering" required!

If you want to find out how to train your own Stable Diffusion variants, see this [example](https://github.com/LambdaLabsML/examples/tree/main/stable-diffusion-finetuning) from Lambda Labs.

![pk1.jpg](https://staticassetbucket.s3.us-west-1.amazonaws.com/grid_output_naruto.png)
> "Face of President Obama smiling", "Face of President Donald Trump", "Face of President Joe Biden"

## Usage

```bash
!pip install diffusers==0.3.0
!pip install transformers scipy ftfy
```

```python
import torch
from diffusers import StableDiffusionPipeline
from torch import autocast

pipe = StableDiffusionPipeline.from_pretrained("eolecvk/sd-naruto-diffusers", torch_dtype=torch.float16)  
pipe = pipe.to("cuda")

prompt = "Yoda"
scale = 10
n_samples = 4

# Sometimes the nsfw checker is confused by the Naruto images, you can disable
# it at your own risk here
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

## Model description

Trained on [BLIP captioned Pokémon images](https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions) using 2xA6000 GPUs on [Lambda GPU Cloud](https://lambdalabs.com/service/gpu-cloud) for around 30,000 step (about 12 hours, at a cost of about $20).

## Links

- [Lambda Diffusers](https://github.com/LambdaLabsML/lambda-diffusers)
- [Captioned Naruto dataset](https://huggingface.co/datasets/eolecvk/naruto-blip-captions)
- [Model weights in Diffusers format](https://huggingface.co/eolecvk/sd-naruto-diffusers)
- [Original model weights](https://huggingface.co/justinpinkney/pokemon-stable-diffusion)
- [Training code](https://github.com/justinpinkney/stable-diffusion)

Trained by Eole Cervenka after the work of [Justin Pinkney](justinpinkney.com) ([@Buntworthy](https://twitter.com/Buntworthy)) at [Lambda Labs](https://lambdalabs.com/).