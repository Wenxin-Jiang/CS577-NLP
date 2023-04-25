---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: creativeml-openrail-m
inference: true

---

# artstation-diffusion v1.0 - Diffusion for normal people.

artstation-diffusion is a latent text-to-image diffusion model that has been conditioned on high-quality Artstation images through fine-tuning.

**Aspect Ratio Bucketing has been used during finetuning. This model can generate different aspect ratios VERY WELL.**

<img src=https://i.imgur.com/otjGl6o.png width=75% height=75%>

<sub>knight, full body study, concept art, atmospheric</sub>

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

## Downstream Uses

This model can be used for entertainment purposes and as a generative art assistant.

## Example Code

```python
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    'hakurei/artstation-diffusion',
    torch_dtype=torch.float32
).to('cuda')

prompt = "knight, full body study, concept art, atmospheric"
with autocast("cuda"):
    image = pipe(prompt, guidance_scale=6).images[0]  
    
image.save("test.png")
```

## Team Members and Acknowledgements

- [Anthony Mercurio](https://github.com/harubaru)

In order to reach me, you can join my [Discord server](https://discord.gg/touhouai).

[![Discord Server](https://discordapp.com/api/guilds/930499730843250783/widget.png?style=banner2)](https://discord.gg/touhouai)