---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---

DISCLAIMER! This Is A Preservation Repository!

# Anything V3 - Better VAE

Welcome to Anything V3 - Better VAE. It currently has three model formats: diffusers, ckpt, and safetensors. You'll never see a grey image result again. This model is designed to produce high-quality, highly detailed anime-style images with just a few prompts. Like other anime-style Stable Diffusion models, it also supports danbooru tags for image generation.
e.g. **_1girl, white hair, golden eyes, beautiful eyes, detail, flower meadow, cumulonimbus clouds, lighting, detailed sky, garden_** 

## Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run Anything V3 with Better VAE:

[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/Linaqruf/Linaqruf-anything-v3-better-vae)

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion). You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

You should install dependencies below in order to running the pipeline

```bash
pip install diffusers transformers accelerate scipy safetensors
```
Running the pipeline (if you don't swap the scheduler it will run with the default DDIM, in this example we are swapping it to DPMSolverMultistepScheduler):

```python
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

model_id = "Linaqruf/anything-v3-0-better-vae"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

prompt = "masterpiece, best quality, illustration, beautiful detailed, finely detailed, dramatic light, intricate details, 1girl, brown hair, green eyes, colorful, autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden"
negative_prompt = "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name"

with autocast("cuda"):
    image = pipe(prompt, 
                 negative_prompt=negative_prompt, 
                 width=512,
                 height=640,
                 guidance_scale=12,
                 num_inference_steps=50).images[0]
    
image.save("anime_girl.png")
```

## Examples

Below are some examples of images generated using this model:

**Anime Girl:**
![Anime Girl](https://huggingface.co/AdamOswald1/anything-v5.0/resolve/main/samples/1girl.png)

**Anime Boy:**
![Anime Boy](https://huggingface.co/AdamOswald1/anything-v5.0/resolve/main/samples/1boy.png)

**Scenery:**
![Scenery](https://huggingface.co/AdamOswald1/anything-v5.0/resolve/main/samples/scenery.png)


## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

# Announcement

For (unofficial) continuation of this model, please visit [andite/anything-v4.0](https://huggingface.co/andite/anything-v4.0). I am aware that the repo exists because I am literally the one who (accidentally) gave the idea to publish his fine-tuned model ([andite/yohan-diffusion](https://huggingface.co/andite/yohan-diffusion)) as a base and merged it with many mysterious model, "hey, let's call it 'Anything V4.0'", because the quality is quite similar to Anything V3 but upgraded.

I also wanted to tell you something. I had a plan to remove/make private one of each repo named "Anything V3":
- [Linaqruf/anything-v3.0](https://huggingface.co/Linaqruf/anything-v3.0/)
- [Linaqruf/anything-v3-better-vae](https://huggingface.co/Linaqruf/anything-v3-better-vae)

Because there are two versions now and I'm late to realize this mysterious non-sense model is already polluted Huggingface Trending for so long, and now when the new repo comes out it is also there. I feel guilty everytime this model is in trending leaderboard.

I prefer to delete/make private this one and let us slowly move to [Linaqruf/anything-v3-better-vae](https://huggingface.co/Linaqruf/anything-v3-better-vae) with better repo management and a better VAE included in the model. 

Please share your thoughts in this #133 discussion about whether I should delete this repo or another one, or maybe both of them.

Thanks,
Linaqruf.

---

# Anything V3

Welcome to Anything V3 - a latent diffusion model for weebs. This model is intended to produce high-quality, highly detailed anime style with just a few prompts. Like other anime-style Stable Diffusion models, it also supports danbooru tags to generate images.

e.g. **_1girl, white hair, golden eyes, beautiful eyes, detail, flower meadow, cumulonimbus clouds, lighting, detailed sky, garden_** 

## Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run Anything-V3.0:

[Open in Spaces](https://huggingface.co/spaces/akhaliq/anything-v3.0)



## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Linaqruf/anything-v3.0"
branch_name= "diffusers"

pipe = StableDiffusionPipeline.from_pretrained(model_id, revision=branch_name, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "pikachu"
image = pipe(prompt).images[0]

image.save("./pikachu.png")
```

## Examples

Below are some examples of images generated using this model:

**Anime Girl:**
![Anime Girl](https://huggingface.co/AdamOswald1/anything-v5.0/resolve/main/1girl.png)
```
1girl, brown hair, green eyes, colorful, autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden
Steps: 50, Sampler: DDIM, CFG scale: 12
```
**Anime Boy:**
![Anime Boy](https://huggingface.co/AdamOswald1/anything-v5.0/resolve/main/1boy.png)
```
1boy, medium hair, blonde hair, blue eyes, bishounen, colorful, autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden
Steps: 50, Sampler: DDIM, CFG scale: 12
```
**Scenery:**
![Scenery](https://huggingface.co/AdamOswald1/anything-v5.0/resolve/main/scenery.png)
```
scenery, shibuya tokyo, post-apocalypse, ruins, rust, sky, skyscraper, abandoned, blue sky, broken window, building, cloud, crane machine, outdoors, overgrown, pillar, sunset
Steps: 50, Sampler: DDIM, CFG scale: 12
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)