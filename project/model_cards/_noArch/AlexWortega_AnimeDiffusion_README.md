---
language:
- en
tags:
- Vintedois (22h) Diffusion model
- text-to-image
license: creativeml-openrail-m
inference: true
library_name: diffusers
---

![image](test.jpg)
<sub>pink hair guy in glasses, photograph, sporty body, cinematic lighting, clear eyes, perfect face, blush,  beautiful nose, beautiful eyes, detailed eyes</sub>


# Anime Diffusion

Anime Diffusion2 is a latent text-to-image diffusion model based on Vintedois (22h) Diffusion model  trained on BLIP captions for Danbou set + Demon slayer + arts from 4ch



## Model Description

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
    'AlexWortega/AnimeDiffuion2',
    torch_dtype=torch.float32
).to('cuda')

negative_prompt = """low-res, duplicate, poorly drawn face, ugly, undetailed face"""
d = 'white girl'
prompt = f"pink hair guy in glasses, photograph, sporty body, cinematic lighting, clear eyes, perfect face, blush,  beautiful nose, beautiful eyes, detailed eyes" 
num_samples = 1

with  torch.inference_mode():
    images = pipe([prompt] * num_samples,
                  negative_prompt = [negative_prompt]*num_samples,
                  height=512, width=512,
                  num_inference_steps=50,
                  guidance_scale=8,
                  ).images


    
images[0].save("test.png")
```

## Team Member and Acknowledgements

This project would not have been possible without the incredible work by the [CompVis Researchers](https://ommer-lab.com/).

- [Alex Wortega](https://github.com/AlexWortega)
<sub>alexwortega@yandex.ru</sub>


In order to reach me, here is my blog:

[![My tg channel]](https://t.me/lovedeathtransformers)