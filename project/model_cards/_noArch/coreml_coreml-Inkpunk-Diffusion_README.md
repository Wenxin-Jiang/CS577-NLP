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

# Inkpunk Diffusion

Finetuned Stable Diffusion model trained on dreambooth. Vaguely inspired by Gorillaz, FLCL, and Yoji Shinkawa. Use **_nvinkpunk_** in your prompts.

# Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run Inkpunk-Diffusion:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/akhaliq/Inkpunk-Diffusion)

# Sample images
![output Samples v2](https://huggingface.co/Envvi/Inkpunk-Diffusion/resolve/main/inkpunk-v2-samples-1.png)
![output Samples v2](https://huggingface.co/Envvi/Inkpunk-Diffusion/resolve/main/inkpunk-v2-samples-2.png)