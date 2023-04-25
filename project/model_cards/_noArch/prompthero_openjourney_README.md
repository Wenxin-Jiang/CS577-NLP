---
inference: true
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
license: creativeml-openrail-m
---
# Openjourney is an open source Stable Diffusion fine tuned model on Midjourney images, by [PromptHero](https://prompthero.com/poolsuite-diffusion-prompts?utm_source=huggingface&utm_medium=referral)

Include **'mdjrny-v4 style'** in prompt. Here you'll find hundreds of [Openjourney prompts](https://prompthero.com/openjourney-prompts?utm_source=huggingface&utm_medium=referral)

# Openjourney Links
- [Lora version](https://huggingface.co/prompthero/openjourney-lora)
- [Openjourney v4](https://huggingface.co/prompthero/openjourney-v2)

# Want to learn AI art generation?:
- [Crash course in AI art generation](https://prompthero.com/academy/prompt-engineering-course?utm_source=huggingface&utm_medium=referral)
- [Learn to fine-tune Stable Diffusion for photorealism](https://prompthero.com/academy/dreambooth-stable-diffusion-train-fine-tune-course?utm_source=huggingface&utm_medium=referral)

# Use it for free:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/akhaliq/midjourney-v4-diffusion)

### Stable Diffusion v1.5 vs Openjourney 
(Same parameters, just added "mdjrny-v4 style" at the beginning):
<img src="https://s3.amazonaws.com/moonup/production/uploads/1667904587642-63265d019f9d19bfd4f45031.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1667904587623-63265d019f9d19bfd4f45031.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1667904587609-63265d019f9d19bfd4f45031.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1667904587646-63265d019f9d19bfd4f45031.png" width="100%"/>

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch
model_id = "prompthero/openjourney"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "retro serie of different cars with different colors and shapes, mdjrny-v4 style"
image = pipe(prompt).images[0]
image.save("./retro_cars.png")
```