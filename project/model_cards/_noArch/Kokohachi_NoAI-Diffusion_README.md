---
license: creativeml-openrail-m
tags:
  - stable-diffusion
  - stable-diffusion-diffusers
  - text-to-image
  - NoAI
  - AntiAI
---

## NoAI-Diffusion v1.2
Updates: prompt now is **antiai logo**

# .CKPT at /models 


# Stable Diffusion 1.4 finetuned with a lot of NoAI/AntiAI images. Have fun 🤗 
## Sample image

v1.0 → normal

v1.1 → *creative*

v1.2 → __clear letters__

NoAI-Diffusion v1.0

||||
|-|-|-|
|![sample 1](https://s3.amazonaws.com/moonup/production/uploads/1671424627294-6304d89ddae2eb7d08416301.jpeg)|![sample 2](https://s3.amazonaws.com/moonup/production/uploads/1671424627497-6304d89ddae2eb7d08416301.jpeg)|![sample 3](https://s3.amazonaws.com/moonup/production/uploads/1671293023842-6305db1fcfbde33ef7d480ff.jpeg)|
|![sample 4](https://s3.amazonaws.com/moonup/production/uploads/1671293062238-6305db1fcfbde33ef7d480ff.jpeg)|![sample 5](https://s3.amazonaws.com/moonup/production/uploads/1671293089847-6305db1fcfbde33ef7d480ff.jpeg)|![sample 6](https://s3.amazonaws.com/moonup/production/uploads/1671293118335-6305db1fcfbde33ef7d480ff.jpeg)|

## Diffusers

```py
from diffusers import StableDiffusionPipeline
import torch
model_id = "Kokohachi/NoAI-Diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to("cuda")
prompt = "a photo of antiai logo"
image = pipe(prompt).images[0]  
    
image.save("noai.png")
```
For more detailed instructions, use-cases and examples in JAX follow the instructions [here](https://github.com/huggingface/diffusers#text-to-image-generation-with-stable-diffusion)


