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

`split_einsum` version is compatible with all compute unit options including Neural Engine.<br>
`original` version is only compatible with CPU & GPU option.

Unfortunately, for this model the `split_einsum` version did not generate images correctly and was removed.

# Dreamlike Diffusion 1.0 is SD 1.5 fine tuned on high quality art, made by [dreamlike.art](https://dreamlike.art/).

Use the same prompts as you would for SD 1.5. Add **dreamlikeart** if the artstyle is too weak.    
Non-square aspect ratios work better for some prompts. If you want a portrait photo, try using a 2:3 or a 9:16 aspect ratio. If you want a landscape photo, try using a 3:2 or a 16:9 aspect ratio.  
Use slightly higher resolution for better results: 640x640px, 512x768px, 768x512px, etc.  

### Examples

<img src="https://huggingface.co/dreamlike-art/dreamlike-diffusion-1.0/resolve/main/preview.jpg" style="max-width: 800px;" width="100%"/>
<img src="https://huggingface.co/dreamlike-art/dreamlike-diffusion-1.0/resolve/main/1.jpg" style="max-width: 800px;" width="100%"/>
<img src="https://huggingface.co/dreamlike-art/dreamlike-diffusion-1.0/resolve/main/2.jpg" style="max-width: 800px;" width="100%"/>

### dreamlike.art

You can use this model for free on [dreamlike.art](https://dreamlike.art/)!

<img src="https://huggingface.co/dreamlike-art/dreamlike-photoreal-1.0/resolve/main/dreamlike.jpg" style="max-width: 1000px;" width="100%"/>

### Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run dreamlike-diffusion-1.0:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/akhaliq/dreamlike-diffusion-1.0)

### CompVis

[Download dreamlike-diffusion-1.0.ckpt (2.13GB)](https://huggingface.co/dreamlike-art/dreamlike-diffusion-1.0/resolve/main/dreamlike-diffusion-1.0.ckpt)

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion Pipeline](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "dreamlike-art/dreamlike-diffusion-1.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "dreamlikeart, a grungy woman with rainbow hair, travelling between dimensions, dynamic pose, happy, soft eyes and narrow chin, extreme bokeh, dainty figure, long hair straight down, torn kawaii shirt and baggy jeans, In style of by Jordan Grimmer and greg rutkowski, crisp lines and color, complex background, particles, lines, wind, concept art, sharp focus, vivid colors"
image = pipe(prompt).images[0]

image.save("./result.jpg")
```

# License

This model is licesed under a **modified** CreativeML OpenRAIL-M license.

- **You can't host or use the model or its derivatives on websites/apps/etc., from which you earn, will earn, or plan to earn revenue or donations. If you want to, please email us at contact@dreamlike.art**
- **You are free to host the model card and files (Without any actual inference or finetuning) on both commercial and non-commercial websites/apps/etc.  Please state the full model name (Dreamlike Diffusion 1.0) and include a link to the model card (https://huggingface.co/dreamlike-art/dreamlike-diffusion-1.0)**  
- **You are free to host the model or its derivatives on completely non-commercial websites/apps/etc (Meaning you are not getting ANY revenue or donations). Please state the full model name (Dreamlike Diffusion 1.0) and include a link to the model card (https://huggingface.co/dreamlike-art/dreamlike-diffusion-1.0)**
- **You are free to use the outputs of the model or the outputs of the model's derivatives for commercial purposes in teams of 10 or less**
- You can't use the model to deliberately produce nor share illegal or harmful outputs or content
- The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
- You may re-distribute the weights. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the **modified** CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully) Please read the full license here: https://huggingface.co/dreamlike-art/dreamlike-diffusion-1.0/blob/main/LICENSE.md
