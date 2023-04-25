---
language:
- en
thumbnail: "https://huggingface.co/wavymulder/wavyfusion/resolve/main/images/page1.jpg"
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---



**Wavyfusion**
![Header](https://huggingface.co/wavymulder/wavyfusion/resolve/main/images/page1.jpg)
[*CKPT DOWNLOAD LINK*](https://huggingface.co/wavymulder/wavyfusion/resolve/main/wa-vy-fusion_1.0.ckpt) - This is a dreambooth trained on a very diverse dataset ranging from photographs to paintings. The goal was to make a varied, general purpose model for illustrated styles.

In your prompt, use the activation token: `wa-vy style`

# Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run wavyfusion:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/akhaliq/wavyfusion)

We use wa-vy instead of wavy because 'wavy style' introduced unwanted oceans and wavy hair.

Trained from 1.5 with VAE.

There are a lot of cool styles you can achieve with this model. [Please see this document where I share the parameters (prompt, sampler, seed, etc.) used for all example images.](https://huggingface.co/wavymulder/wavyfusion/resolve/main/prompts_for_examples.md)

![Character Example](https://huggingface.co/wavymulder/wavyfusion/resolve/main/images/page2.jpg)
![Landscape Example](https://huggingface.co/wavymulder/wavyfusion/resolve/main/images/page3.jpg)

[And here is an batch of 49 images (not cherrypicked) in both euler_a and DPM++ 2M Karras](https://imgur.com/a/rBft6mw)

Special thanks to [Nitrosocke](https://huggingface.co/nitrosocke) and [Guizmus](https://huggingface.co/Guizmus)

