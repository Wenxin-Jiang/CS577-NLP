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

# Poison Model

Welcome to poison model. This model is intended to produce high-quality, highly detailed anime style with just a few prompts. Unlike other anime style models, it has a little realistic style(but not too much), especially in the character painting.

It's finetuned from [anything model](https://huggingface.co/Linaqruf/anything-v3.0),and merge back to anything after training.

This model is converted from [poison](https://huggingface.co/Fansy/poison)

Compare result:

![](image1.jpg)

# Usage

```
import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler

repo_id = "mrdabin/poison"
pipe = DiffusionPipeline.from_pretrained(repo_id, torch_dtype=torch.float16, revision="fp16")
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

prompt = "High quality photo of an astronaut riding a horse in space"
image = pipe(prompt, num_inference_steps=25).images[0]
image.save("astronaut.png")
```

# License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage. The CreativeML OpenRAIL License specifies:

You can't use the model to deliberately produce nor share illegal or harmful outputs or content
The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully) Please read the full license here