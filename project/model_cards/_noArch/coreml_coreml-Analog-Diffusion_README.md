---
license: creativeml-openrail-m
tags:
- coreml
- stable-diffusion
- text-to-image
---

# Core ML Converted Model

This model was converted to Core ML for use on Apple Silicon devices by following Apple's instructions [here](https://github.com/apple/ml-stable-diffusion#-converting-models-to-core-ml).<br>
Provide the model to an app such as [Mochi Diffusion](https://github.com/godly-devotion/MochiDiffusion) to generate images.<br>

`split_einsum` version is compatible with all compute unit options including Neural Engine.<br>
`original` version is only compatible with CPU & GPU option.

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
