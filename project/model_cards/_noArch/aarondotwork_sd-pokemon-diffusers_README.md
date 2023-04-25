---
language: 
  - en
thumbnail: "https://s3.amazonaws.com/moonup/production/uploads/1663756797814-62bd5f951e22ec84279820e8.png"
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
datasets:
- lambdalabs/pokemon-blip-captions
---

**This copy of the Lambda Labs model only adds the fp16 branch for compatibility with the Stable Cabal GRPC server**

__Stable Diffusion fine tuned on Pokémon by [Lambda Labs](https://lambdalabs.com/).__

Put in a text prompt and generate your own Pokémon character, no "prompt engineering" required!

If you want to find out how to train your own Stable Diffusion variants, see this [example](https://github.com/LambdaLabsML/examples/tree/main/stable-diffusion-finetuning) from Lambda Labs.


![image.png](https://s3.amazonaws.com/moonup/production/uploads/1663756797814-62bd5f951e22ec84279820e8.png)

> Girl with a pearl earring, Cute Obama creature, Donald Trump, Boris Johnson, Totoro, Hello Kitty

## Usage

```bash
!pip install diffusers==0.3.0
!pip install transformers scipy ftfy
```

```python
import torch
from diffusers import StableDiffusionPipeline
from torch import autocast

pipe = StableDiffusionPipeline.from_pretrained("lambdalabs/sd-pokemon-diffusers", torch_dtype=torch.float16)  
pipe = pipe.to("cuda")

prompt = "Yoda"
scale = 10
n_samples = 4

# Sometimes the nsfw checker is confused by the Pokémon images, you can disable
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

Trained on [BLIP captioned Pokémon images](https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions) using 2xA6000 GPUs on [Lambda GPU Cloud](https://lambdalabs.com/service/gpu-cloud) for around 15,000 step (about 6 hours, at a cost of about $10).

## Links

- [Lambda Diffusers](https://github.com/LambdaLabsML/lambda-diffusers)
- [Captioned Pokémon dataset](https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions)
- [Model weights in Diffusers format](https://huggingface.co/lambdalabs/sd-pokemon-diffusers)
- [Original model weights](https://huggingface.co/justinpinkney/pokemon-stable-diffusion)
- [Training code](https://github.com/justinpinkney/stable-diffusion)

Trained by [Justin Pinkney](justinpinkney.com) ([@Buntworthy](https://twitter.com/Buntworthy)) at [Lambda Labs](https://lambdalabs.com/).