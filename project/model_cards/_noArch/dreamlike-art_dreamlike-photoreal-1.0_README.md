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

# This 1.0 model is OBSOLETE. We've released a new much better 2.0 version!

**Check it out here: [https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0](https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0)**

<img src="https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/preview1.jpg" style="max-width: 800px;" width="100%"/>


Dreamlike Photoreal 1.0 is a photorealistic Stable Diffusion 1.5 model fine tuned on high quality photos, made by [dreamlike.art](https://dreamlike.art/).

Use the same prompts as you would for photorealistic SD 1.5 gens. You can also use danbooru style tags for characters (1girl, brown hair, etc.).  
Non-square aspect ratios work better for some prompts. If you want a portrait photo, try using a 3:4 or a 9:16 aspect ratio. If you want a landscape photo, try using a 16:9 aspect ratio.

### Examples

<img src="https://huggingface.co/dreamlike-art/dreamlike-photoreal-1.0/resolve/main/preview.jpg" style="max-width: 800px;" width="100%"/>

### dreamlike.art

You can use this model for free on [dreamlike.art](https://dreamlike.art/)!

<img src="https://huggingface.co/dreamlike-art/dreamlike-photoreal-1.0/resolve/main/dreamlike.jpg" style="max-width: 1000px;" width="100%"/>

### CompVis

[Download dreamlike-photoreal-1.0.ckpt (2.13GB)](https://huggingface.co/dreamlike-art/dreamlike-photoreal-1.0/resolve/main/dreamlike-photoreal-1.0.ckpt)

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion Pipeline](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "dreamlike-art/dreamlike-photoreal-1.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "caucasian creative man wearing a sweater, sitting, on an icelandic beach"
image = pipe(prompt).images[0]

image.save("./result.jpg")
```

# License

This model is licesed under a **modified** CreativeML OpenRAIL-M license.

- **You can't host or use the model or its derivatives on websites/apps/etc., from which you earn, will earn, or plan to earn revenue or donations. If you want to, please email us at contact@dreamlike.art**
- **You are free to host the model card and files (Without any actual inference or finetuning) on both commercial and non-commercial websites/apps/etc.  Please state the full model name (Dreamlike Photoreal 1.0) and include a link to the model card (https://huggingface.co/dreamlike-art/dreamlike-photoreal-1.0)**  
- **You are free to host the model or its derivatives on completely non-commercial websites/apps/etc (Meaning you are not getting ANY revenue or donations). Please state the full model name (Dreamlike Photoreal 1.0) and include a link to the model card (https://huggingface.co/dreamlike-art/dreamlike-photoreal-1.0)**
- **You are free to use the outputs of the model or the outputs of the model's derivatives for commercial purposes in teams of 10 or less**
- You can't use the model to deliberately produce nor share illegal or harmful outputs or content
- The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
- You may re-distribute the weights. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the **modified** CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully) Please read the full license here: https://huggingface.co/dreamlike-art/dreamlike-photoreal-1.0/blob/main/LICENSE.md
