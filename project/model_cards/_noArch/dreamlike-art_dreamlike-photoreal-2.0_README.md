---
language:
- en
license: other
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- photorealistic
- photoreal
- diffusers
inference: false
---

# Dreamlike Photoreal 2.0 is a photorealistic model based on Stable Diffusion 1.5, made by [dreamlike.art](https://dreamlike.art/).  
  
# If you want to use dreamlike models on your website/app/etc., check the license at the bottom first!  

Warning: This model is horny! Add "nude, naked" to the negative prompt if want to avoid NSFW.  
  
You can add **photo** to your prompt to make your gens look more photorealistic.   
Non-square aspect ratios work better for some prompts. If you want a portrait photo, try using a vertical aspect ratio. If you want a landscape photo, try using a horizontal aspect ratio.  
This model was trained on 768x768px images, so use 768x768px, 640x896px, 896x640px, etc. It also works pretty good with higher resolutions such as 768x1024px or 1024x768px.  

### Examples

<img src="https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/preview1.jpg" style="max-width: 800px;" width="100%"/>
<img src="https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/preview2.jpg" style="max-width: 800px;" width="100%"/>
<img src="https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/preview3.jpg" style="max-width: 800px;" width="100%"/>

### dreamlike.art

You can use this model for free on [dreamlike.art](https://dreamlike.art/)!

<img src="https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/dreamlike.jpg" style="max-width: 1000px;" width="100%"/>

### CKPT

[Download dreamlike-photoreal-2.0.ckpt (2.13GB)](https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/dreamlike-photoreal-2.0.ckpt)

### Safetensors
[Download dreamlike-photoreal-2.0.safetensors (2.13GB)](https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/dreamlike-photoreal-2.0.safetensors)

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion Pipeline](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "dreamlike-art/dreamlike-photoreal-2.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "photo, a church in the middle of a field of crops, bright cinematic lighting, gopro, fisheye lens"
image = pipe(prompt).images[0]

image.save("./result.jpg")
```

<img src="https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/church.jpg" style="max-width: 640px;" width="100%"/>

# License

This model is licesed under a **modified** CreativeML OpenRAIL-M license.

- **You are not allowed to host, finetune, or do inference with the model or its derivatives on websites/apps/etc. If you want to, please email us at contact@dreamlike.art**
- **You are free to host the model card and files (Without any actual inference or finetuning) on both commercial and non-commercial websites/apps/etc.  Please state the full model name (Dreamlike Photoreal 2.0) and include the license as well as a link to the model card (https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0)**  
- **You are free to use the outputs (images) of the model for commercial purposes in teams of 10 or less**
- You can't use the model to deliberately produce nor share illegal or harmful outputs or content
- The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
- You may re-distribute the weights. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the **modified** CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully) Please read the full license here: https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/blob/main/LICENSE.md
