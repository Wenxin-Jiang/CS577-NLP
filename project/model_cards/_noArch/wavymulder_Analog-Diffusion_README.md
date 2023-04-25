---
language:
- en
thumbnail: "https://huggingface.co/wavymulder/Analog-Diffusion/resolve/main/images/page1.jpg"
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- safetensors
- diffusers
inference: true
---



**Analog Diffusion**
![Header](https://huggingface.co/wavymulder/Analog-Diffusion/resolve/main/images/page1.jpg)
[*CKPT DOWNLOAD LINK*](https://huggingface.co/wavymulder/Analog-Diffusion/resolve/main/analog-diffusion-1.0.ckpt) - This is a dreambooth model trained on a diverse set of analog photographs.

In your prompt, use the activation token: `analog style`

You may need to use the words `blur` `haze` `naked` in your negative prompts. My dataset did not include any NSFW material but the model seems to be pretty horny. Note that using `blur` and `haze` in your negative prompt can give a sharper image but also a less pronounced analog film effect.

Trained from 1.5 with VAE.

Please see [this document where I share the parameters (prompt, sampler, seed, etc.) used for all example images.](https://huggingface.co/wavymulder/Analog-Diffusion/resolve/main/parameters_used_examples.txt)

## Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run Analog-Diffusion:

[Open in Spaces](https://huggingface.co/spaces/akhaliq/Analog-Diffusion)


![Environments Example](https://huggingface.co/wavymulder/Analog-Diffusion/resolve/main/images/page2.jpg)
![Characters Example](https://huggingface.co/wavymulder/Analog-Diffusion/resolve/main/images/page3.jpg)

Here's a [link to non-cherrypicked batches.](https://imgur.com/a/7iOgTFv)
