---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---
This is the fine-tuned Stable Diffusion model trained on screenshots from The Clone wars TV series. Use the tokens "Clonewars style" in your prompts for the effect.

**If you enjoy my work, please consider supporting me:**
[![Follow me on Twitter](https://badgen.net/badge/Follow/me/blue)](https://twitter.com/GeeeWilllikers)
[![Buy me a coffee](https://badgen.net/badge/buy/Coffee/F96854)](https://ko-fi.com/trystar)

## Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI run CloneDiffusion:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/akhaliq/CloneDiffusion)

**Star Wars Characters**
![Star Wars Characters](https://huggingface.co/TryStar/CloneDiffusion/resolve/main/Starwars.jpg)


**How to use?**

Use prompt "clonewars style" before your full prompt.

I recommend Steps: 50, Sampler: Euler a and CFG scale: 7

This model was trained using the diffusers based dreambooth training by [TheLastBen](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb)