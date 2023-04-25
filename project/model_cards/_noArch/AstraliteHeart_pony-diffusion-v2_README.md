---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: bigscience-bloom-rail-1.0
inference: false
thumbnail: "https://cdn.discordapp.com/attachments/1020199895694589953/1020200601780494386/000001.553325548.png"
---

# pony-diffusion-v2 - more anthro edition

**[Pony Diffusion V4 is now live!](https://huggingface.co/AstraliteHeart/pony-diffusion-v4)**

pony-diffusion is a latent text-to-image diffusion model that has been conditioned on high-quality pony and furry SFW and NSFW images through fine-tuning.

WARNING: Compared to v1 of this model, v2 is much more capable of producing NSFW content so it's recommended to use 'safe' tag in prompt in combination with negative prompt for image features you may want to suppress. v2 model also has a slight 3d bias so negative prompts like '3d' or 'sfm' should be used to better match v1 outputs.  

With special thanks to [Waifu-Diffusion](https://huggingface.co/hakurei/waifu-diffusion) for providing finetuning expertise and [Novel AI](https://novelai.net/) for providing necessary compute.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mSharzQFPD4mIUxNwBG7LCLAzGUS8Bmy?usp=sharing)

[![Join Discord Server to try next generation models](https://discordapp.com/api/guilds/670866322619498507/widget.png?style=banner2)](https://discord.gg/pYsdjMfu3q)

<img src=https://cdn.discordapp.com/attachments/704107851421057114/1035464229001646110/image0.png width=50% height=50%>
<img src=https://cdn.discordapp.com/attachments/704107851421057114/1035450288145965086/00053-4009799064-Fluttershy_wearing_a_hoodie_cute_detailed_high_res_4k_trending_on_art_station_art_by_greg.png width=50% height=50%>
<img src=https://cdn.discordapp.com/attachments/704107851421057114/1035466996097232956/upscaled_safe_pumpkin_orange_body_spots_on_bod-1.webp width=50% height=50%>


[Original PyTorch Model Download Link](https://mega.nz/file/Va0Q0B4L#QAkbI2v0CnPkjMkK9IIJb2RZTegooQ8s6EpSm1S4CDk)

[Real-ESRGAN Model finetuned on pony faces](https://mega.nz/folder/cPMlxBqT#aPKYrEfgA_lpPexr0UlQ6w)

## Model Description

The model originally used for fine-tuning is an early finetuned checkpoint of [waifu-diffusion](https://huggingface.co/hakurei/waifu-diffusion) on top of [Stable Diffusion V1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4), which is a latent image diffusion model trained on [LAION2B-en](https://huggingface.co/datasets/laion/laion2B-en).

This particular checkpoint has been fine-tuned with a learning rate of 5.0e-6 for 4 epochs on approximately 450k pony and furry text-image pairs (using tags from derpibooru and e621) which all have score greater than `250`.

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
model_id = "AstraliteHeart/pony-diffusion-v2"
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