---
inference: true
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
license: creativeml-openrail-m
---

# Corporate Memphis is a finetuned Stable Diffusion model by [@jinofcoolnes](https://twitter.com/jinofcoolnes)

Use prompt: 'Corporate_Memphis digital illustration'


### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion) documentation.

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch
model_id = "jinofcoolnes/corporate_memphis"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "coliseum full of different cars with different colors and shapes; Corporate_Memphis digital illustration"
image = pipe(prompt).images[0]
image.save("./cars.png")
```