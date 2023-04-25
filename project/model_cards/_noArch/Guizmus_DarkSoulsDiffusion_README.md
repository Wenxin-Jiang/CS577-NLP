---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Guizmus/DarkSoulsDiffusion/resolve/main/showcase.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: true
---

# DarkSouls Diffusion
<p>
	<img src="https://huggingface.co/Guizmus/DarkSoulsDiffusion/resolve/main/showcase.jpg"/><br/>
	This is a Dreamboothed Stable Diffusion model trained on the DarkSouls series Style.<br/>
	The total dataset is made of 100 pictures, and the training has been done on runawayml 1.5 and the new VAE, with 2500 steps (LR1e-6) then 24k more steps (LR1e-7).<br/>
	The token "DarkSouls Style" will bring in the new concept.<br/>
	The recommended sampling is k_Euler_a or DPM++ 2M Karras on 20 steps, CFGS 7 .
	
</p>

[CKPT download link](https://huggingface.co/Guizmus/DarkSoulsDiffusion/resolve/main/DarkSoulsStyle_v1-3.ckpt)

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Guizmus/DarkSoulsDiffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a soldier engulfed in fire, DarkSouls Style"
image = pipe(prompt).images[0]

image.save("./DarkSouls Style.png")
```