---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: unknown
datasets:
- Danbooru2021
inference: true

---

## Repo Overview

A version of Waifu Diffusion v1.4 Float32 Booru 110k model and VAE from Waifu Diffusion v1.4 converted to work with Diffusers library.

![](https://files.catbox.moe/hqfckc.png)
^ Quality/Style test

![](https://files.catbox.moe/eac57m.png)
^ Unnatural resolution test

![](https://files.catbox.moe/ulrm28.png)
^ Landscape test

![](https://files.catbox.moe/odvq06.png)
^ Extremely long resolution test

## Model Description

The current model has been fine-tuned on a Stable Diffusion 2.1 model with 110k anime-styled images using a technique known as aspect ratio bucketing.

That allows Waifu Diffusion v1.4 to handle different resolutions much better than its previous models.

## Source

WD v1.4 Model:https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/9fa4a42a9c4a0948472fa909e6c1a39be0dda699/models/wd-1-4-float32-booru-110k.ckpt

WD v1.4 VAE: https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/vae/kl-f8-anime2.ckpt