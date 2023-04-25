---
language: 
  - en
thumbnail: ""
tags:
- painting
- anime
- stable-diffusion
- aiart
- text-to-image
license: creativeml-openrail-m
---
<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/0Style-Girl.png" width="700" height="559"/></center>

![visitors](https://visitor-badge.glitch.me/badge?page_id=DGspitzer_Art_Diffusion)

# DGSpitzer Art Diffusion

DGSpitzer Art Diffusion is **a unique AI model that is trained to draw like my art style!**

# Online Demo

You can try the Online Web UI demo build with Gradio:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/DGSpitzer/DGS-Diffusion-Space)

Hello folks! This is DGSpitzer, I'm a game developer, music composer and digital artist based in New York, you can check out my artworks/games/etc at here:
[Games](https://helixngc7293.itch.io/) 
[Arts](https://www.artstation.com/helixngc7293) 
[Music](https://soundcloud.com/dgspitzer) 

I've been working on AI related stuff on my [Youtube  Channel](https://www.youtube.com/channel/UCzzsYBF4qwtMwJaPJZ5SuPg) 
 since 2020 , especially for colorizing old black & white footage using a series of AI technologies.

I always portrait artificial intelligence as an assist tool for extending my creativity. Nevertheless, whatever how powerful AI will be, us humans will be the leading role during the creative process as usual, and AI will provide suggestions / generate drafts as a helper.
In my opinion, there is huge potential to adapt AI into the modern-age digital artist's work pipeline, therefore I trained this AI model with my art style as an experiment to try it out! And **share it with you for free!**

All of the datasets (as the training images for building this AI model) is from my own digital paintings & game concept arts, no other artists’ names involved. I separated my artworks into detailed categories such as “outline”, “sketch”, “anime”, “landscape”. As a result, **this AI model supports multiple keywords in prompt as different styles of mine!**
The model is fine-tuned based on [Vintedois diffusion-v0-1 Model](https://huggingface.co/22h/vintedois-diffusion-v0-1/) though, but I totally overwrite the style of the vintedois diffusion model by using “arts”, “paintings” as keywords with my dataset during Dreambooth training.

**You are free to use/fine-tune this model even commercially as long as you follow the [CreativeML Open RAIL-M license](LICENSE).** Additionally, **you can use all my artworks as dataset in your training**, giving a credit should be cool ;P

It’s welcome to share your results using this model! Looking forward to creating something truly amazing!

*Buy me a coffee if you like this project ;P ♥*
[![Buy me a coffee](https://badgen.net/badge/icon/Buy%20Me%20A%20Coffee?icon=buymeacoffee&label)](https://www.buymeacoffee.com/dgspitzer)


<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/1Style-Girl2.png" width="700" height="559"/></center>

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/2Style-Man.png" width="700" height="559"/></center>

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/3Style-Outline.png" width="700" height="559"/></center>

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/4Style-Anime.png" width="700" height="559"/></center>

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/5Style-Whiteshape.png" width="700" height="559"/></center>

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/6Style-Sketch.png" width="700" height="559"/></center>

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/7Style-Landscape.png" width="700" height="559"/></center>

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/8Style-Mech.png" width="700" height="559"/></center>


### 🧨 Diffusers

This repo contains both .ckpt and Diffuser model files. It's compatible to be used as any Stable Diffusion model, using standard [Stable Diffusion Pipelines](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can convert this model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX](https://huggingface.co/blog/stable_diffusion_jax).

```python example for loading the Diffuser
#!pip install diffusers transformers scipy torch
from diffusers import StableDiffusionPipeline
import torch

model_id = "DGSpitzer/DGSpitzer-Art-Diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "dgspitzer painting of a beautiful mech girl, 4k, photorealistic"
image = pipe(prompt).images[0]

image.save("./dgspitzer_ai_art.png")
```


# **👇Model👇**

AI Model Weights available at huggingface: https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion


# Usage

After model loaded, there are multiple keywords supported (represent as different styles):

**painting** a general style from my paintings, good for portraits

**outline** a character painting with outline and flat color, slight anime style

**landscape** general landscape style

**anime** cute simple anime characters

**whiteshape** a character with stylized white color body silhouette and pure color background

**sketch** a sketch style from my draft paintings

**arts** & **dgspitzer** extra prompts work as **painting** keyword to create the general style of my paintings


For sampler, use **DPM++ SDE Karras** or **Euler A** for the best result (**DDIM** kinda works too), CFG Scale 7, steps 20 should be fine

**Example 1:**

```
dgspitzer painting portrait of a girl, draw photorealistic painting full body portrait of stunningly attractive female soldier working, cleavage, perfect face, dark ponytail curvy hair, intricate, 8k, highly detailed, shy, digital painting, intense, sharp focus
```

**Example 2:**

```
outline anime portrait of a beautiful martial art girl
```

**Example 3 (with Stable Diffusion WebUI):**

If using [AUTOMATIC1111's Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

You can simply use this as **prompt** with **Euler A** Sampler,  CFG Scale 7, steps 20, 704 x 704px output res:

```
an anime girl with cute face holding an apple in dessert island
```

And always recommend to set the **negative prompt** as similar to this to get much better result: 

```
lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, bad feet
```

If the result too purple/colorful (which I draw quite a lot...), you can add this keyword in the **negative prompt** as well:

```
saturation, purple, red
```

---

**NOTE: usage of this model implies accpetance of stable diffusion's [CreativeML Open RAIL-M license](LICENSE)**

---

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/00033.jpg" width="700" height="700"/></center>

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/00054.jpg" width="700" height="700"/></center>

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/00052-2.jpg" width="700" height="1050"/></center>

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/00093.jpg" width="700" height="963"/></center>

<center><img src="https://huggingface.co/DGSpitzer/DGSpitzer-Art-Diffusion/resolve/main/img/00956.jpg" width="700" height="700"/></center>
