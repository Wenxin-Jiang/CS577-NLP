---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: bigscience-bloom-rail-1.0
inference: false

---

# waifu-diffusion - Diffusion for Weebs

waifu-diffusion is a latent text-to-image diffusion model that has been conditioned on high-quality anime images through fine-tuning.

# Gradio

We also support a [Gradio](https://github.com/gradio-app/gradio) web ui with diffusers to run inside a colab notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_8wPN7dJO746QXsFnB09Uq2VGgSRFuYE#scrollTo=1HaCauSq546O)

<img src=https://cdn.discordapp.com/attachments/930559077170421800/1017265913231327283/unknown.png width=40% height=40%>

[Original PyTorch Model Download Link](https://thisanimedoesnotexist.ai/downloads/wd-v1-2-full-ema.ckpt)

## Model Description

The model originally used for fine-tuning is [Stable Diffusion V1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4), which is a latent image diffusion model trained on [LAION2B-en](https://huggingface.co/datasets/laion/laion2B-en).

The current model has been fine-tuned with a learning rate of 5.0e-6 for 4 epochs on 56k text-image pairs obtained through Danbooru which all have an aesthetic rating greater than `6.0`.

**Note:** This project has **no affiliation with Danbooru.**

## Training Data & Annotative Prompting

The data used for fine-tuning has come from a random sample of 56k Danbooru images, which were filtered based on [CLIP Aesthetic Scoring](https://github.com/christophschuhmann/improved-aesthetic-predictor) where only images with an aesthetic score greater than `6.0` were used.

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
from diffusers import StableDiffusionPipeline, DDIMScheduler

model_id = "hakurei/waifu-diffusion"
device = "cuda"


pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    revision="fp16",
    scheduler=DDIMScheduler(
        beta_start=0.00085,
        beta_end=0.012,
        beta_schedule="scaled_linear",
        clip_sample=False,
        set_alpha_to_one=False,
    ),
)
pipe = pipe.to(device)

prompt = "touhou hakurei_reimu 1girl solo portrait"
with autocast("cuda"):
    image = pipe(prompt, guidance_scale=7.5)["sample"][0]  
    
image.save("reimu_hakurei.png")
```

## Team Members and Acknowledgements

This project would not have been possible without the incredible work by the [CompVis Researchers](https://ommer-lab.com/).

- [Anthony Mercurio](https://github.com/harubaru)
- [Salt](https://github.com/sALTaccount/)
- [Sta @ Bit192](https://twitter.com/naclbbr)

In order to reach us, you can join our [Discord server](https://discord.gg/touhouai).

[![Discord Server](https://discordapp.com/api/guilds/930499730843250783/widget.png?style=banner2)](https://discord.gg/touhouai)