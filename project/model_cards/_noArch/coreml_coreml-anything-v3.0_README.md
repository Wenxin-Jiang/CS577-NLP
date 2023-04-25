---
license: creativeml-openrail-m
tags:
- coreml
- stable-diffusion
- text-to-image
---

# Core ML Converted Model

This model was converted to Core ML for use on Apple Silicon devices by following Apple's instructions [here](https://github.com/apple/ml-stable-diffusion#-converting-models-to-core-ml).<br>
Provide the model to an app such as [Mochi Diffusion](https://github.com/godly-devotion/MochiDiffusion) to generate images.<br>

`split_einsum` versions are compatible with all compute units.<br>
`original` versions are only compatible with CPU & GPU.

# Anything V3

Sources: [Hugging Face](https://huggingface.co/Linaqruf/anything-v3.0) - [CivitAI](https://civitai.com/models/66/anything-v3)</br>
The first source model is the first published model at the Hugging Face link above. The current source model is anything-v3-better-vae model which is now published at the same Hugging Face link.

Welcome to Anything V3 - a latent diffusion model for weebs. This model is intended to produce high-quality, highly detailed anime style with just a few prompts. Like other anime-style Stable Diffusion models, it also supports danbooru tags to generate images.

e.g. **_1girl, white hair, golden eyes, beautiful eyes, detail, flower meadow, cumulonimbus clouds, lighting, detailed sky, garden_** 

## Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run Anything-V3.0:

[Open in Spaces](https://huggingface.co/spaces/Maseshi/Anything-v3.0)

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Maseshi/Anything-v3.0"
branch_name = "diffusers"

pipe = StableDiffusionPipeline.from_pretrained(model_id, revision=branch_name, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "pikachu"
image = pipe(prompt).images[0]

image.save("./pikachu.png")
```

## Examples

Below are some examples of images generated using this model:

**Anime Girl:**
![Anime Girl](https://huggingface.co/Maseshi/Anything-v3.0/resolve/main/1girl.png)
```
1girl, brown hair, green eyes, colorful, autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden
Steps: 50, Sampler: DDIM, CFG scale: 12
```
**Anime Boy:**
![Anime Boy](https://huggingface.co/Maseshi/Anything-v3.0/resolve/main/1boy.png)
```
1boy, medium hair, blonde hair, blue eyes, bishounen, colorful, autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden
Steps: 50, Sampler: DDIM, CFG scale: 12
```
**Scenery:**
![Scenery](https://huggingface.co/Maseshi/Anything-v3.0/resolve/main/scenery.png)
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