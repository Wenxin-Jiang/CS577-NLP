---
license: creativeml-openrail-m
tags:
  - stable-diffusion
  - stable-diffusion-diffusers
  - text-to-image
  - NoAI
  - AntiAI
---

Stable Diffusion 1.4 finetuned with a lot of NoAI/AntiAI images plus AI generated **creative** logos. Have fun 🤗 

## Sample image

NoAI-Diffusion-variety v1.0

||||
|-|-|-|
|![sample.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1671372814032-6304d89ddae2eb7d08416301.jpeg)|
## Diffusers

```py
from diffusers import StableDiffusionPipeline
import torch
model_id = "Kokohachi/NoAI-Diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to("cuda")
prompt = "sks icon, antiai logo"
image = pipe(prompt).images[0]  
    
image.save("noai.png")
```
For more detailed instructions, use-cases and examples in JAX follow the instructions [here](https://github.com/huggingface/diffusers#text-to-image-generation-with-stable-diffusion)

