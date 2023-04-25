---
language:
- en
thumbnail: >-
  https://huggingface.co/AdamOswald1/Cyberpunk-Anime-Diffusion/resolve/main/img/thumbnail.png
tags:
- cyberpunk
- anime
- stable-diffusion
- aiart
- text-to-image
- TPU
license: creativeml-openrail-m
library_name: diffusers
datasets:
- Nerfgun3/cyberware_style
- Nerfgun3/bad_prompt
---
<center><img src="https://huggingface.co/AdamOswald1/Cyberpunk-Anime-Diffusion/resolve/main/img/5.jpg" width="512" height="512"/></center>

![visitors](https://visitor-badge.glitch.me/badge?page_id=Cyberpunk_Anime_Diffusion)

# Cyberpunk Anime Diffusion

An AI model that generates cyberpunk anime characters!~

Based of a finetuned Waifu Diffusion V1.3 Model with Stable Diffusion V1.5 New Vae, training in Dreambooth

by [DGSpitzer](https://www.youtube.com/channel/UCzzsYBF4qwtMwJaPJZ5SuPg)

### 🧨 Diffusers

This repo contains both .ckpt and Diffuser model files. It's compatible to be used as any Stable Diffusion model, using standard [Stable Diffusion Pipelines](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can convert this model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX](https://huggingface.co/blog/stable_diffusion_jax).

```python example for loading the Diffuser
#!pip install diffusers transformers scipy torch
from diffusers import StableDiffusionPipeline
import torch
model_id = "AdamOswald1/Cyberpunk-Anime-Diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "a beautiful perfect face girl in dgs illustration style, Anime fine details portrait of school girl in front of modern tokyo city landscape on the background deep bokeh, anime masterpiece, 8k, sharp high quality anime"
image = pipe(prompt).images[0]
image.save("./cyberpunk_girl.png")
```

# Online Demo

You can try the Online Web UI demo build with [Gradio](https://github.com/gradio-app/gradio), or use Colab Notebook at here:

*My Online Space Demo*
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/DGSpitzer/DGS-Diffusion-Space)

*Finetuned Diffusion WebUI Demo by anzorq*
[![Use Finetuned_Diffusion WebUI](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/anzorq/finetuned_diffusion)

*Colab Notebook*
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HelixNGC7293/cyberpunk-anime-diffusion/blob/main/cyberpunk_anime_diffusion.ipynb)[![GitHub](https://badgen.net/badge/icon/Github?icon=github&label)](https://github.com/HelixNGC7293/cyberpunk-anime-diffusion)

*Buy me a coffee if you like this project ;P ♥*
[![Buy me a coffee](https://badgen.net/badge/icon/Buy%20Me%20A%20Coffee?icon=buymeacoffee&label)](https://www.buymeacoffee.com/dgspitzer)

<center><img src="https://huggingface.co/AdamOswald1/Cyberpunk-Anime-Diffusion/resolve/main/img/1.jpg" width="512" height="512"/></center>

# **👇Model👇**

AI Model Weights available at huggingface: https://huggingface.co/AdamOswald1/Cyberpunk-Anime-Diffusion

<center><img src="https://huggingface.co/AdamOswald1/Cyberpunk-Anime-Diffusion/resolve/main/img/2.jpg" width="512" height="512"/></center>

# Usage

After model loaded, use keyword **dgs** in your prompt, with **illustration style** to get even better results.

For sampler, use **Euler A** for the best result (**DDIM** kinda works too), CFG Scale 7, steps 20 should be fine

**Example 1:**

```
portrait of a girl in dgs illustration style, Anime girl, female soldier working in a cyberpunk city, cleavage, ((perfect femine face)), intricate, 8k, highly detailed, shy, digital painting, intense, sharp focus
```

For cyber robot male character, you can add **muscular male** to improve the output.

**Example 2:**

```
a photo of muscular beard soldier male in dgs illustration style, half-body, holding robot arms, strong chest
```

**Example 3 (with Stable Diffusion WebUI):**

If using [AUTOMATIC1111's Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

You can simply use this as **prompt** with **Euler A** Sampler,  CFG Scale 7, steps 20, 704 x 704px output res:

```
an anime girl in dgs illustration style
```

And set the **negative prompt** as this to get cleaner face: 

```
out of focus, scary, creepy, evil, disfigured, missing limbs, ugly, gross, missing fingers
```

This will give you the exactly same style as the sample images above.

<center><img src="https://huggingface.co/AdamOswald1/Cyberpunk-Anime-Diffusion/resolve/main/img/ReadmeAddon.jpg" width="256" height="353"/></center>

---

**NOTE: usage of this model implies accpetance of stable diffusion's [CreativeML Open RAIL-M license](LICENSE)**

---


<center><img src="https://huggingface.co/AdamOswald1/Cyberpunk-Anime-Diffusion/resolve/main/img/4.jpg" width="700" height="700"/></center>

<center><img src="https://huggingface.co/AdamOswald1/Cyberpunk-Anime-Diffusion/resolve/main/img/6.jpg" width="700" height="700"/></center>