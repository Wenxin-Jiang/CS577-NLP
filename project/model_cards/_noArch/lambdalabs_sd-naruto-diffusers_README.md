---
language: 
  - en
thumbnail: "https://staticassetbucket.s3.us-west-1.amazonaws.com/GOT_naruto.png"
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
datasets:
- lambdalabs/naruto-blip-captions
---

# Naruto diffusion
*Stable Diffusion fine tuned on Naruto by [Lambda Labs](https://lambdalabs.com/).*

__Try the live [text-to-naruto demo here](https://huggingface.co/spaces/lambdalabs/text-to-naruto)!__  
If you want more details on how to train your own Stable Diffusion variants, see this [example](https://github.com/LambdaLabsML/examples/tree/main/stable-diffusion-finetuning).

## About

Put in a text prompt and generate your own Naruto style image!

**Game of Thrones to Naruto**

![pk0.jpg](https://staticassetbucket.s3.us-west-1.amazonaws.com/GOT_naruto.png)

**Marvel to Naruto**

![pk1.jpg](https://staticassetbucket.s3.us-west-1.amazonaws.com/marvel_naruto.png)

## Prompt engineering matters

We find that prompt engineering does help produce compelling and consistent Naruto style portraits.
For example, writing prompts such as '*person_name* ninja portrait' or '*person_name* in the style of Naruto' tends to produce results that are closer to the style of Naruto character with the characteristic headband and other elements of costume.

Here are a few examples of prompts with and without prompt engineering that will illustrate that point.

**Bill Gates:**
![pk2.jpg](https://staticassetbucket.s3.us-west-1.amazonaws.com/bill_gates_vanilla.png)
> Without prompt engineering

![pk3.jpg](https://staticassetbucket.s3.us-west-1.amazonaws.com/bill_gates_ninja.png)
> With prompt engineering

**A cute bunny:**

![pk4.jpg](https://staticassetbucket.s3.us-west-1.amazonaws.com/cute_bunny_vanilla.png)
> Without prompt engineering

![pk4.jpg](https://staticassetbucket.s3.us-west-1.amazonaws.com/cute_bunny_ninja.png)
> With prompt engineering



## Usage

To run model locally:
```bash
!pip install diffusers==0.3.0
!pip install transformers scipy ftfy
```

```python
import torch
from diffusers import StableDiffusionPipeline
from torch import autocast

pipe = StableDiffusionPipeline.from_pretrained("lambdalabs/sd-naruto-diffusers", torch_dtype=torch.float16)  
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

Trained on [BLIP captioned Naruto images](https://huggingface.co/datasets/lambdalabs/naruto-blip-captions) using 2xA6000 GPUs on [Lambda GPU Cloud](https://lambdalabs.com/service/gpu-cloud) for around 30,000 step (about 12 hours, at a cost of about $20).

## Links


- [Lambda Diffusers](https://github.com/LambdaLabsML/lambda-diffusers)
- [Captioned Naruto dataset](https://huggingface.co/datasets/lambdalabs/naruto-blip-captions)
- [Model weights in Diffusers format](https://huggingface.co/lambdalabs/sd-naruto-diffusers)
- [Original model weights](https://huggingface.co/justinpinkney/pokemon-stable-diffusion)
- [Naruto diffusers repo](https://github.com/eolecvk/naruto-sd)

Trained by [Eole Cervenka](https://www.linkedin.com/in/eole-cervenka/) after the work of [Justin Pinkney](https://justinpinkney.com) ([@Buntworthy](https://twitter.com/Buntworthy)) at [Lambda Labs](https://lambdalabs.com/).