---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: bigscience-bloom-rail-1.0
inference: true
thumbnail: "https://cdn.discordapp.com/attachments/1020199895694589953/1020200601780494386/000001.553325548.png"
---

# pony-diffusion - >nohooves

**[Pony Diffusion V4 is now live!](https://huggingface.co/AstraliteHeart/pony-diffusion-v4)**

pony-diffusion is a latent text-to-image diffusion model that has been conditioned on high-quality pony SFW-ish images through fine-tuning.

With special thanks to [Waifu-Diffusion](https://huggingface.co/hakurei/waifu-diffusion) for providing finetuning expertise and [Novel AI](https://novelai.net/) for providing necessary compute.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/10Naa1SiIy0CA7bjk0q1rCcMMza6aWXpy?usp=sharing)

[![Join Discord Server to try next generation models](https://discordapp.com/api/guilds/670866322619498507/widget.png?style=banner2)](https://discord.gg/pYsdjMfu3q)

<img src=https://cdn.discordapp.com/attachments/1020199895694589953/1020200601780494386/000001.553325548.png width=50% height=50%>
<img src=https://cdn.discordapp.com/attachments/1020199895694589953/1020213899175415858/unknown.png width=50% height=50%>
<img src=https://cdn.discordapp.com/attachments/1020199895694589953/1021448446072340520/unknown.png width=50% height=50%>
<img src=https://cdn.discordapp.com/attachments/704226060178292846/1018644965905141840/upscaled_100_pony_made_of_rough_ivy_.webp width=50% height=50%>


[Original PyTorch Model Download Link](https://mega.nz/file/ZT1xEKgC#Xxir5udMmU_mKaRZAbBkF247Yk7DqCr01V0pDzSlYI0)

[Real-ESRGAN Model finetuned on pony faces](https://mega.nz/folder/cPMlxBqT#aPKYrEfgA_lpPexr0UlQ6w)

## Model Description

The model originally used for fine-tuning is an early finetuned checkpoint of [waifu-diffusion](https://huggingface.co/hakurei/waifu-diffusion) on top of [Stable Diffusion V1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4), which is a latent image diffusion model trained on [LAION2B-en](https://huggingface.co/datasets/laion/laion2B-en).

This particular checkpoint has been fine-tuned with a learning rate of 5.0e-6 for 4 epochs on approximately 80k pony text-image pairs (using tags from derpibooru) which all have score greater than `500` and belong to categories `safe` or `suggestive`.

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
model_id = "AstraliteHeart/pony-diffusion"
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
prompt = "pinkie pie anthro portrait wedding dress veil intricate highly detailed digital painting artstation concept art smooth sharp focus illustration Unreal Engine 5 8K"
with autocast("cuda"):
    image = pipe(prompt, guidance_scale=7.5)["sample"][0]  
    
image.save("cute_poner.png")
```

## Team Members and Acknowledgements

This project would not have been possible without the incredible work by the [CompVis Researchers](https://ommer-lab.com/).

- [Waifu-Diffusion for helping with finetuning and providing starting checkpoint](https://huggingface.co/hakurei/waifu-diffusion)
- [Novel AI for providing compute](https://novelai.net/)

In order to reach us, you can join our [Discord server](https://discord.gg/WG78ZbSB).