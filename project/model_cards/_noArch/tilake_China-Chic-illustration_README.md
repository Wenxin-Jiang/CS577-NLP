---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- wildcard
widget:
- text: >-
    a rabbit wearing sunglasses, in the style of <guo-chao> illustration,
    trending on artstation, masterpiece, best quality
language:
- zh
- en
---


# DreamBooth model for China-Chic-illustration

This is the first model for `China-Chic illustration` (国潮插画) style painting. The model is based on Stable Diffusion model, fine-tuned the `China-Chic illustration` style taught to Stable Diffusion with DreamBooth. It is trained by tilake AIGC group on the own dataset.
It can be used by modifying the `instance_prompt`: **style of \<guo-chao\> illustration**

全球首个 “国潮插画” 风格定制化模型发布。该模型基于 Stable Diffusion model，并采用 DreamBooth 微调。该模型由 TiLake AIGC Group 在内部数据集上训练而来。  
你可以通过扩充以下 `instance_prompt` 来使用国潮插画模型绘制各种画作: **style of \<guo-chao\> illustration**

# Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run China-Chic-illustration:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/akhaliq/China-Chic-illustration)


## Description

This is a Stable Diffusion model fine-tuned on `China-Chic illustration` style images. It is trained by Tilake AIGC Group.   
If you like this model, click the \[❤ like\]  button!

国潮插画是将传统文化和现代潮流审美进行结合的一种插画形式，开放该模型旨在给相关艺术家和工作者提供灵感和创作思路。如果喜欢该模型，欢迎点亮网页最上方的【like】按钮~

## Examples
- Prompt: ```a cute rabbit in red clothes, in the style of <guo-chao> illustration, trending on artstation, masterpiece, best quality```（国潮兔）
  <img width="200px" height="200px" src="https://huggingface.co/tilake/China-Chic-illustration/resolve/main/example/1.jpg">
- Prompt: ```dragon dance, in the style of <guo-chao> illustration, trending on artstation, masterpiece, best quality```（国潮舞龙）
  <img width="200px" height="200px" src="https://huggingface.co/tilake/China-Chic-illustration/resolve/main/example/2.jpg">
- Prompt: ```fireworks, in the style of <guo-chao> illustration, trending on artstation, masterpiece, best quality```（国潮烟花）
  <img width="200px" height="200px" src="https://huggingface.co/tilake/China-Chic-illustration/resolve/main/example/3.jpg">
- Prompt: ```a snowman, fireworks in the background, in the style of <guo-chao> illustration, trending on artstation, masterpiece, best quality```（国潮雪人）
  <img width="200px" height="200px" src="https://huggingface.co/tilake/China-Chic-illustration/resolve/main/example/4.jpg">
  
## Usage

```python
from diffusers import StableDiffusionPipeline

# guidance_scale=8.8 may be the best
pipeline = StableDiffusionPipeline.from_pretrained('tilake/China-Chic-illustration')
image = pipeline("style of <guo-chao> illustration, a rabbit wearing sunglasses").images[0]
image
```